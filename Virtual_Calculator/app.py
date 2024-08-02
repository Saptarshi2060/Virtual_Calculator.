import cv2
import mediapipe as mp
import numpy as np
import easyocr
import sympy as sp
from collections import deque

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize OCR Reader
reader = easyocr.Reader(['en'])

# Set up drawing variables
drawing = False
drawing_image = np.zeros((480, 640, 3), dtype=np.uint8)
prev_x, prev_y = None, None

# History stacks for undo and redo
drawing_history = deque(maxlen=50)
redo_stack = deque(maxlen=50)

# Function to preprocess image for OCR
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    return binary

# Function to recognize text
def recognize_text(image):
    results = reader.readtext(image)
    text = ''.join([res[1] for res in results])
    return text

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to make it mirror-like
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * 640), int(index_finger_tip.y * 480)

            if drawing:
                if prev_x is not None and prev_y is not None:
                    cv2.line(drawing_image, (prev_x, prev_y), (x, y), (255, 255, 255), 2)
                prev_x, prev_y = x, y
            else:
                prev_x, prev_y = None, None

    # Combine the frame with the drawing image
    combined_frame = cv2.addWeighted(frame, 1, drawing_image, 1, 0)

    cv2.imshow('Virtual Calculator', combined_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('d'):
        drawing = not drawing
    elif key == ord('c'):
        drawing_image = np.zeros((480, 640, 3), dtype=np.uint8)
        drawing_history.clear()
        redo_stack.clear()
    elif key == ord('q'):
        break
    elif key == ord('u'):
        if drawing_history:
            redo_stack.append(drawing_image.copy())
            drawing_image = drawing_history.pop()
    elif key == ord('r'):
        if redo_stack:
            drawing_history.append(drawing_image.copy())
            drawing_image = redo_stack.pop()
    elif key == ord('s'):
        drawing_history.append(drawing_image.copy())
        binary_drawing = preprocess_image(drawing_image)
        text = recognize_text(binary_drawing)
        try:
            expr = sp.sympify(text)
            result = expr.evalf()
            print(f'Recognized: {text}, Result: {result}')
            cv2.putText(drawing_image, f'Result: {result}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f'Recognized: {text}, Result: Error - {e}')
            cv2.putText(drawing_image, 'Result: Error', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cap.release()
cv2.destroyAllWindows()

# Virtual Calculator with Air Writing Detection

This project implements a virtual calculator that uses hand gestures captured by a webcam to detect and process mathematical expressions drawn in the air. The application uses MediaPipe for hand tracking, OpenCV for image processing, EasyOCR for text recognition, and SymPy for mathematical evaluation.

## Features

- **Hand Gesture Recognition**: Detects hand movements to draw numbers and mathematical symbols in the air.
- **Drawing on Screen**: Displays the drawn mathematical expressions on the screen.
- **Undo/Redo Functionality**: Allows undoing and redoing the most recent drawing actions using keyboard shortcuts.
- **Expression Recognition**: Recognizes drawn mathematical expressions and evaluates them.
- **Real-Time Results**: Displays the result of the evaluated mathematical expression on the screen.

  ## Usuage
  
- **Toggle Drawing: Press d to start or stop drawing with hand gestures.
- **Clear Drawing: Press c to clear the current drawing and reset the history.
- **Undo Action: Press u to undo the last drawing action.
- **Press r to redo the last undone drawing action.
- **Recognize and Solve Expression: Press s to recognize the drawn expression, evaluate it, and display the result.
- **Exit Application: Press q to quit the application.
- **Open your webcam and start drawing mathematical expressions in the air. The application will display your drawing and calculate the result of the recognized expression.

## Technology Used
  
- **Python: Core programming language used for development.
- **Libraries:
- **OpenCV: For image and video processing.
- **MediaPipe: For hand gesture recognition.
- **EasyOCR: For text recognition from the drawn image.
- **SymPy: For evaluating mathematical expressions.
- **Webcam: Used to capture hand gestures in real-time.
- **Troubleshooting
- **Ensure good lighting and a clear view of your hand for accurate tracking.
- **Adjust the webcam position to capture your hand gestures properly.
- **If the recognition is not accurate, try drawing slower and more clearly.


## Setup

To set up and run the virtual calculator locally, follow these steps:

```bash
# Clone the repository
git clone <repository-url>
cd virtual-calculator

# Install dependencies
pip install opencv-python mediapipe easyocr sympy

# Run the application
python virtual_calculator.py



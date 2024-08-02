# Virtual Calculator with Air Writing Detection

This project implements a virtual calculator that uses hand gestures captured by a webcam to detect and process mathematical expressions drawn in the air. The application uses MediaPipe for hand tracking, OpenCV for image processing, EasyOCR for text recognition, and SymPy for mathematical evaluation.

## Features

- **Hand Gesture Recognition**: Detects hand movements to draw numbers and mathematical symbols in the air.
- **Drawing on Screen**: Displays the drawn mathematical expressions on the screen.
- **Undo/Redo Functionality**: Allows undoing and redoing the most recent drawing actions using keyboard shortcuts.
- **Expression Recognition**: Recognizes drawn mathematical expressions and evaluates them.
- **Real-Time Results**: Displays the result of the evaluated mathematical expression on the screen.

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

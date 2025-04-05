from eyeGestures.utils import VideoCapture
from eyeGestures import EyeGestures_v3
import os

# Initialize gesture engine and video capture
gestures = EyeGestures_v3()
cap = VideoCapture(0)
calibrate = True
screen_width = 1080
screen_height= 1920

# Process each frame
while True:
  ret, frame = cap.read()
  event, cevent = gestures.step(frame,
    calibrate,
    screen_width,
    screen_height,
    context="my_context")

  if event:
    cursor_x, cursor_y = event.point[0], event.point[1]
    fixation = event.fixation
    saccades = event.saccades # saccadess movement detector
    # calibration_radius: radius for data collection during calibration
    print(event.point)
    os.system(f'sudo -S ydotool mousemove -a {cursor_x} {1920-cursor_y}')

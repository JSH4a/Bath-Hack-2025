from random import random

from ultralytics import YOLO
import cv2
import numpy as np
import time
import os
# import pyautogui

model = YOLO('best.pt')

# Open a connection to the webcam
cap = cv2.VideoCapture(2)  # Change the index if needed
previous_position = [540, 960]  # Initial position of the mouse cursor
while True:


    ret, frame = cap.read()
    if not ret:
        break

    # Send the frame to the model for inference
    try:
        results = model(frame, verbose=False)
    except:
        continue
    # Display the results
    for result in results:
        fingers_tensor = result.keypoints.xyn.cpu()[0]
        if len(fingers_tensor) == 0:
            continue
        fingertips = [fingers_tensor[i] for i in [8, 12, 16] if fingers_tensor[i][1] > 0]
        if not fingertips:
            continue
        mean_fingertip = np.mean(fingertips, axis=0)

        # Scale the mean_fingertip position to the monitor size (1920x1080)
        screen_x = int((1- mean_fingertip[0]) * 1080)
        screen_y = int(mean_fingertip[1] * 1920)
        # Move the mouse cursor to the scaled position using ydotool

        # Calculate the distance between the previous and current positions
        distance = np.linalg.norm(np.array(previous_position) - np.array([screen_x, screen_y]))
        # If the distance is greater than a threshold, move the mouse
        # print(distance)
        if distance > 15:
            # print(f'sudo ydotool mousemove -x {previous_position[0] - screen_x} {previous_position[1] - screen_y}')
            os.system(f'sudo ydotool mousemove -x {(screen_x - previous_position[0]) * 1.1} -y {(screen_y - previous_position[1])* 1.1}')
            # os.system(f'sudo ydotool mousemove -a -x {(screen_x )} -y {(screen_y )}')

            previous_position = screen_x, screen_y
    # Display the frame
    # cv2.imshow('YOLO Inference', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

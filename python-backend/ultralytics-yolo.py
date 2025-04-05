from ultralytics import YOLO
import cv2
import numpy as np
import time

model = YOLO('best.pt')

# Open a connection to the webcam
cap = cv2.VideoCapture(2)

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
        screen_x = int((1-mean_fingertip[0]) * 1080)
        screen_y = int(mean_fingertip[1] * 1920)

        # Move the mouse cursor to the scaled position
        print(screen_x, screen_y)

    # Display the frame
    cv2.imshow('YOLO Inference', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

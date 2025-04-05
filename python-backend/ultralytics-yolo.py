from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

# Open a connection to the webcam
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Send the frame to the model for inference
    results = model(frame)

    # Display the results
    for result in results:
        # Assuming result has a method to plot or draw the detections
        print(result.keypoints.xyn)

    # Display the frame
    cv2.imshow('YOLO Inference', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

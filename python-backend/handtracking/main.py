async def run(websocket):
    print("hey ghosters")
    import cv2
    import mediapipe as mp
    import time
    from subprocess import call
    import numpy as np
    import json
    import websockets
    import asyncio
    
    INDEX_FINGER_IDX = 8
    THUMB_IDX = 4
    VOLUME_UPDATE_INTERVAL = 15
    HOZ = 1920
    VER = 1080
    
    CAM_MAX_X=640
    CAM_MAX_Y=480
    
    #opening camera (0 for the default camera)
    videoCap = cv2.VideoCapture(0)
    lastFrameTime = 0
    frame = 0
    max_diff = 0
    min_diff = 100000
    handSolution = mp.solutions.hands
    hands = handSolution.Hands()
    prev_x = 0
    prev_y = 0
    actual_x = -1
    actual_y = -1
    while True:
        frame += 1
        #reading image
        success, img = videoCap.read()
        #showing image on separate window (only if read was successfull)
        if success:
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #fps calculations
            thisFrameTime = time.time()
            fps = 1 / (thisFrameTime - lastFrameTime)
            lastFrameTime = thisFrameTime
            #write on image fps
            cv2.putText(img, f'FPS:{int(fps)}',
                        (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            #recognize hands from out image
            recHands = hands.process(img)
            if recHands.multi_hand_landmarks:
                for hand in recHands.multi_hand_landmarks:
                    #draw the dots on each our image for vizual help
                    for datapoint_id, point in enumerate(hand.landmark):
                        h, w, c = img.shape
                        x, y = int(point.x * w), int(point.y * h)
                        cv2.circle(img, (x, y),
                                5, (255, 0, 255)
                                , cv2.FILLED)
                        # Draw lines between landmarks (connecting points)
                    for i in range(len(hand.landmark) - 1):
                        if i in [4, 8, 12, 16, 20]:
                            continue
                        x1, y1 = int(hand.landmark[i].x * w), int(hand.landmark[i].y * h)
                        x2, y2 = int(hand.landmark[i + 1].x * w), int(hand.landmark[i + 1].y * h)
                        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                for i in [5, 9, 13, 17]:
                    x1, y1 = int(hand.landmark[i].x * w), int(hand.landmark[i].y * h)
                    x2, y2 = int(hand.landmark[0].x * w), int(hand.landmark[0].y * h)
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            if frame % VOLUME_UPDATE_INTERVAL == 0:
                index_y = (hand.landmark[INDEX_FINGER_IDX].y/CAM_MAX_Y)*VER
                distance_y = (index_y * h - prev_y * h)
                index_x = (hand.landmark[INDEX_FINGER_IDX].x/CAM_MAX_X)*HOZ
                distance_x = -1*(index_x * h - prev_x * h)
                if actual_x == -1 or actual_y == -1:
                    actual_x = 0
                    actual_y = 0

                    actual_x += distance_x
                    actual_y += distance_y
                    mp = {'x': 0, 'y': 0}
                    await websocket.send(json.dumps(mp))
                    await asyncio.sleep(0.5)
                    continue
                actual_x += distance_x
                actual_y += distance_y
                mp = {'x': actual_x, 'y': actual_y }
                prev_x = index_x
                prev_y = index_y
                await websocket.send(json.dumps(mp))
                await asyncio.sleep(0.5)
                frame = 0
        cv2.imshow("CamOutput", img)
        cv2.waitKey(1)

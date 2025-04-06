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
    L_CLICK_THRESHOLD=0.005
    
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
            imgRGB = cv2.flip(img, 1)
            #fps calculations
            thisFrameTime = time.time()
            fps = 1 / (thisFrameTime - lastFrameTime)
            lastFrameTime = thisFrameTime
            #write on image fps
            cv2.putText(imgRGB, f'FPS:{int(fps)}',
                        (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            #recognize hands from out image
            recHands = hands.process(imgRGB)
            if recHands.multi_hand_landmarks:
                for hand in recHands.multi_hand_landmarks:
                    #draw the dots on each our image for vizual help
                    for datapoint_id, point in enumerate(hand.landmark):
                        h, w, c = img.shape
                        x, y = int(point.x * w), int(point.y * h)
                        cv2.circle(imgRGB, (x, y),
                                5, (255, 0, 255)
                                , cv2.FILLED)
                        # Draw lines between landmarks (connecting points)
                    for i in range(len(hand.landmark) - 1):
                        if i in [4, 8, 12, 16, 20]:
                            continue
                        x1, y1 = int(hand.landmark[i].x * w), int(hand.landmark[i].y * h)
                        x2, y2 = int(hand.landmark[i + 1].x * w), int(hand.landmark[i + 1].y * h)
                        cv2.line(imgRGB, (x1, y1), (x2, y2), (0, 255, 0), 2)
                for i in [5, 9, 13, 17]:
                    x1, y1 = int(hand.landmark[i].x * w), int(hand.landmark[i].y * h)
                    x2, y2 = int(hand.landmark[0].x * w), int(hand.landmark[0].y * h)
                    cv2.line(imgRGB, (x1, y1), (x2, y2), (0, 255, 0), 2)
                if frame % frame == 0:
                    index_y = (hand.landmark[INDEX_FINGER_IDX].y/CAM_MAX_Y)*VER/1.7
                    distance_y = (index_y * h - prev_y * h)
                    index_x = (hand.landmark[INDEX_FINGER_IDX].x/CAM_MAX_X)*HOZ/2.5
                    distance_x = (index_x * h - prev_x * h)
                    if actual_x == -1 or actual_y == -1:
                        actual_x = 0
                        actual_y = 0
    
                        actual_x += distance_x
                        actual_y += distance_y
                        mp = {'x': 0, 'y': 0, 'click': 0}
                        await websocket.send(json.dumps(mp))
                        await asyncio.sleep(0.001)
                        continue
                    actual_x = index_x
                    actual_y = index_y
                    
                    did_click = 0
                    num_ = (hand.landmark[6].y - hand.landmark[THUMB_IDX].y)**2 + (hand.landmark[6].x - hand.landmark[THUMB_IDX].x)**2 
                    if num_ < L_CLICK_THRESHOLD:
                        print(f"clicked {num_}")
                        did_click = 1
                    mp = {'x': index_x, 'y': index_y, 'click': did_click }
                    prev_x = index_x
                    prev_y = index_y
                    await websocket.send(json.dumps(mp))
                    await asyncio.sleep(0.001)
                    frame = 0
            else:
                mp = {'x': actual_x, 'y': actual_y, 'click': 0 }
                await websocket.send(json.dumps(mp))
                await asyncio.sleep(0.001)
            cv2.imshow("CamOutput", imgRGB)
            cv2.waitKey(1)

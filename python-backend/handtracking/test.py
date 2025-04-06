import asyncio
import websockets
import pyautogui
import json
import time

prev_time = 0
WIDTH, HEIGHT = pyautogui.size()

async def receive_and_move_mouse():
    uri = "ws://172.26.123.88:8765"  # Replace with your Raspberry Pi's IP address
    global prev_time
    global WIDTH
    global HEIGHT
    async with websockets.connect(uri) as websocket:
        while True:
            # Receive mouse position from the server
            message = await websocket.recv()
            position = json.loads(message)
            if time.time() - prev_time > 0.01:
                # Move the mouse to the received position
                x = position['x'] * WIDTH
                y = position['y'] * HEIGHT
                pyautogui.moveTo(x, y)
                if position['click'] == 1:
                    pyautogui.click()
                print(f"Moved mouse to: {position['x']}, {position['y']}")
                prev_time = time.time()

# Start the asyncio event loop
if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    #pyautogui.MINIMUM_DURATION=0.05
    prev_time = time.time()
    asyncio.run(receive_and_move_mouse())
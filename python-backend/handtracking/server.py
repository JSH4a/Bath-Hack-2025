import asyncio
import websockets
import random
import json
from  main import run

async def send_mouse_position(websocket):
    while True:
        mouse_position = {'x': random.randint(0, 1920), 'y': random.randint(0, 1080)}

        await websocket.send(json.dumps(mouse_position))
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(run, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

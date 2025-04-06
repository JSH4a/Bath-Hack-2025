from flask import Flask, request
import pyautogui
import numpy as np
import threading
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Store calibration data (these are the screen positions corresponding to gaze)
calibration_points = []
gaze_points = []

@app.route('/calibrate', methods=['POST'])
def calibrate():
    data = request.get_json()
    calibration_points.append((data['x'], data['y']))
    
    # Once we have 9 points, perform calibration
    if len(calibration_points) == 9:
        print("Calibration complete!")
        return '', 204
    return '', 204

@app.route('/gaze', methods=['POST'])
def move_cursor():
    if len(calibration_points) < 9:
        return '', 400  # Calibration hasn't been completed yet

    data = request.get_json()
    gaze_x, gaze_y = data['x'], data['y']

    # Calculate mouse position based on calibration (mapping gaze -> screen position)
    cursor_x, cursor_y = map_gaze_to_cursor(gaze_x, gaze_y)

    # Move the cursor to the calculated position
    threading.Thread(target=pyautogui.moveTo, args=(cursor_x, cursor_y)).start()
    return '', 204

def map_gaze_to_cursor(gaze_x, gaze_y):
    # Simple linear mapping from gaze to cursor position (assuming it's a 1-to-1 mapping)
    # You could implement a more advanced algorithm (e.g., regression) for better accuracy
    screen_width, screen_height = pyautogui.size()
    
    # Calculate the average of calibration points to estimate a transformation matrix
    calib_xs, calib_ys = zip(*calibration_points)
    avg_calib_x, avg_calib_y = np.mean(calib_xs), np.mean(calib_ys)
    
    # Map gaze (in WebGazer coordinates) to screen coordinates
    cursor_x = (gaze_x - avg_calib_x) * (screen_width / (max(calib_xs) - min(calib_xs))) + (screen_width / 2)
    cursor_y = (gaze_y - avg_calib_y) * (screen_height / (max(calib_ys) - min(calib_ys))) + (screen_height / 2)

    # Ensure the cursor stays within screen bounds
    cursor_x = max(0, min(cursor_x, screen_width))
    cursor_y = max(0, min(cursor_y, screen_height))

    return cursor_x, cursor_y

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

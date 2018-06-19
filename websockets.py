import cv2
import base64
from flask_socketio import emit
from app import socketio


img = cv2.imread('static/images/watch.jpg', cv2.IMREAD_GRAYSCALE)
@socketio.on('connect')
def connect_handler():
    encoded_string = base64.b64encode(img)
    emit('camera', {'meta': encoded_string})

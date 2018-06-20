import cv2
import base64
from flask_socketio import emit
from app import socketio
import numpy as np
# img = cv2.imread('static/images/watch.jpg', cv2.IMREAD_GRAYSCALE)
camera = cv2.VideoCapture(0)
img = cv2.imread('static/images/watch.jpg')
# img = np.load(img)

# with open('static/images/watch.jpg', "rb") as image_file:
#     print(type(image_file.read()))

img = camera.read()[1]
cnt = cv2.imencode('.jpg', img)
print(type(cnt))
print(cnt[1])
encoded_string = base64.encodestring(cnt[1][0])
# encoded_text = base64.b64encode(b'toto')
encoded_text = base64.b64encode(b'toto').decode('ascii')

@socketio.on('connect')
def connect_handler():
    # encoded_string = base64.b64encode(img)
    # encoded_string = base64.encodestring(encoded_string)
    emit('camera', {'text': encoded_text, 'buffer': encoded_string})

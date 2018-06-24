import cv2
import base64
from flask_socketio import emit
from app import socketio
import numpy as np
from io import BytesIO
from PIL import Image
# img = cv2.imread('static/images/watch.jpg', cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture(0)
img = cv2.imread('static/images/watch.jpg')
# img = np.load(img)

# with open('static/images/watch.jpg', "rb") as image_file:
#     print(type(image_file.read()))
def base64_encode(data):
    if data:
        return 'data:image/png;base64,' + data

hello, image = cap.read()
hello, image = cv2.imencode('.jpg', image)
buffer = BytesIO()
img = Image.fromarray(image)
img.save(buffer, format="png")
encoded_string = base64.b64encode(image.tostring())
print(image.tostring())
@socketio.on('connect')
def connect_handler():
    # encoded_string = base64.b64encode(img)
    # encoded_string = base64.encodestring(encoded_string)
    emit('camera', {'buffer': base64_encode(encoded_string)})

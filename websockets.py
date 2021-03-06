import cv2
# from PIL import Image
import base64
from flask_socketio import emit
from app import socketio

img = cv2.imread('static/images/watch.jpg')

"""Sends camera images in an infinite loop."""

retval, buffer = cv2.imencode('.jpg', img)
# With Pillow
# sio = io.StringIO()
# img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
# img.save(sio, "JPEG")
# sio.getValue()

encoded_text = "toto"


@socketio.on('connect')
def connect_handler():
    # encoded_string = base64.b64encode(img)
    # encoded_string = base64.encodestring(encoded_string)
    emit('camera', {'text':  base64.b64encode(encoded_text),
                    'buffer': "data:image/jpeg;base64," +
                    base64.b64encode(buffer)})

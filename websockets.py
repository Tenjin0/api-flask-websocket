import cv2
from flask_socketio import SocketIO, join_room, emit
# import numpy as np
# import tkinter
img = cv2.imread('static/images/watch.jpg', cv2.IMREAD_GRAYSCALE)

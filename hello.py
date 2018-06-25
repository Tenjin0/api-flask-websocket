#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np


def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    print(image)
    image[:] = color
    print(image)
    return image


# Create new blank 300x300 red image
width, height = 2, 2

red = (255, 0, 0)
image = create_blank(width, height, rgb_color=red)
# grey = np.zeros((4, 4, 3), np.uint8)
# print(grey)
cv2.imshow('ImageWindow', image)
cv2.waitKey()

import os
import cv2
import numpy as np

img = cv2.imread('./2.jpg') #파일명

canvas = np.zeros(shape=img.shape, dtype=np.uint8)
canvas.fill(255)
canvas[np.where((img == [1,0,164]).all(axis = 2))] = [255,0,0]

cv2.imwrite('_seoul.png', canvas)
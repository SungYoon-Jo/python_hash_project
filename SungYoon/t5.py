#-*- coding:utf-8 -*-
import cv2
import numpy as np
from skimage.transform import resize

img1 = cv2.imread('./1.jpg')
img2 = cv2.imread('./2.jpg')

res1 = resize(img1, (640,640))
res2 = resize(img2, (640,640))

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while True:

    w = cv2.getTrackbarPos('W','image')

    dst = cv2.addWeighted(res1,float(100-w) * 0.01, res2,float(w) * 0.01,0)

    cv2.imshow('dst', dst)

    if cv2.waitKey(1) &0xFF == 27:
        break;

cv2.destroyAllWindows()
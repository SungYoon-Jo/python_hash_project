from PIL import Image
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

np.set_printoptions(threshold=sys.maxsize)
image =cv2.imread("input.png",0)
plt.imshow(image,cmap='gray')
plt.show()
print(image.shape)
print(type(image))
# print(image)

img_strided = image.reshape(image.shape[0]//4, 4, image.shape[1]//4, 4).swapaxes(1, 2)
print(img_strided.shape)
print(img_strided[0][0])
print(img_strided[0][1])
print(img_strided[1][0])
plt.imshow(image,cmap='gray')
plt.show()
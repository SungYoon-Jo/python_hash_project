# import cv2
# import numpy as np
# from math import floor

# #Load image
# img = cv2.imread('./01.png')
# print(img.shape, img.dtype)
# height = img.shape[0]
# width = img.shape[1]

# #Scale
# target_size = (300, 300)  # target size
# output = np.zeros((target_size[0], target_size[1], 3), np.uint8)

# x_scale = height/output.shape[0]   #input image / output image
# y_scale = width/output.shape[1]   #input image / output image

# for y in range(output.shape[1]):
#     for x in range(output.shape[0]):
#         # the pixel at coordinate (x, y) in the new image is equal to the pixel that is located at coordinate (floor(x * x_ratio), floor(y * y_ratio)).
#         # floor는 인접한 픽셀을 가져오기 위해서 사용
#         xp, yp = floor(x* x_scale), floor(y * y_scale)
#         print(xp, yp)
#         print(x, y)
#         output[x,y] = img[xp,yp]
# cv2.imwrite('./scale.png', output)

import cv2
import numpy as np

img = cv2.imread('./01.png')
height, width = img.shape[:2]

target_size = (300,300)
scale_img = cv2.resize(img, (target_size[0], target_size[1]), \
                         interpolation=cv2.INTER_AREA)

cv2.imwrite('./scale_cv.png', scale_img)
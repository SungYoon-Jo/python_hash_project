import cv2
import sys

img = cv2.imread("./1.jpg")


sys.stdout = open('stdout.txt', 'w')

for i in range(1):
    print(img)

sys.stdout.close()

# print(img.shape)
# print(img.shape[0])
# print(type(img.shape[0]))

# print(type(img))
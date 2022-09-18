import cv2
from skimage.transform import resize


img1 = cv2.imread('./1.jpg')
img2 = cv2.imread('./2.jpg')

res1 = resize(img1, (500,500))
res2 = resize(img2, (500,500))

bit_and = cv2.bitwise_and(res1, res2)
# bit_or = cv2.bitwise_or(res1, res2)
# bit_not = cv2.bitwise_not(res2)
# bit_xor = cv2.bitwise_xor(res1, res2)

# cv2.imshow('res1', res1)
# cv2.imshow('res2', res2)
cv2.imshow('bit_and', bit_and)
# cv2.imshow('bit_or', bit_or)
# cv2.imshow('bit_not', bit_not)
# cv2.imshow('bit_xor', bit_xor)

cv2.waitKey()
cv2.destroyAllWindows()
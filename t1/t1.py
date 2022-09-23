import cv2

print('cv2.__version__:',cv2.__version__)
 
img1 = cv2.imread('./1.jpg') 
img2 = cv2.imread('./2.jpg' ) 
 
img_ret1 = cv2.bitwise_not(img1)
print('img1[161,199]:    ',img1[161,199])
print('img_ret1[161,199]:',img_ret1[161,199])
cv2.imshow('lena-not-juzicode',img_ret1)
 
img_ret2 = cv2.bitwise_not(img2)
print('img2[100,200]:    ',img2[100,200])
print('img_ret2[100,200]:',img_ret2[100,200])
cv2.imshow('logo-not-juzicode',img_ret2)
 
cv2.waitKey(0)
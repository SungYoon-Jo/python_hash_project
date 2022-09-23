import cv2

print('cv2.__version__:',cv2.__version__)
 
img1 = cv2.imread('./1.jpg' )[0:300,0:300]
img_ret1 = cv2.bitwise_and(img1,(0x3f,0x3f,0x3f,0))
print('img1[161,199]:    ',img1[161,199])
print('img_ret1[161,199]:',img_ret1[161,199])
cv2.imshow('and-juzicode',img_ret1) 
 
img_ret2 = cv2.bitwise_or(img1,(0x0f,0x0f,0x0f))
print('img_ret2[161,199]:',img_ret2[161,199])
cv2.imshow('or-juzicode',img_ret2) 
 
img_ret3 = cv2.bitwise_xor(img1,0xf0)
print('img_ret3[161,199]:',img_ret3[161,199])
cv2.imshow('xor-juzicode',img_ret3) 
 
cv2.waitKey(0)
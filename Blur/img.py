
import cv2
import numpy as np
from skimage.transform import resize

win_name = 'Transparency'     # 창 이름
trackbar_name = 'fade'          # 트렉바 이름

# ---① 트렉바 이벤트 핸들러 함수
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(res1, 1-alpha, res2, alpha, 0) 
    cv2.imshow(win_name, dst)


# ---② 합성 영상 읽기
img1 = cv2.imread('./img/1.jpg')
img2 = cv2.imread('./img/2.jpg')
# img2 = cv2.imread('./img/temp.jpg')

res1 = resize(img1, (640,640))
res2 = resize(img2, (640,640))

# ---③ 이미지 표시 및 트렉바 붙이기
cv2.imshow(win_name, res1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()
import cv2

img = cv2.imread("./img/test.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

border, binary =  cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

cv2.imshow("img", img)

cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
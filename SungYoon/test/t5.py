import cv2 as cv


img_color = cv.imread('./img/test.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)


cv.imwrite('1bit_image.png' ,img_binary, [cv.IMWRITE_PNG_BILEVEL, 1])
cv.imwrite('8bit_image.png' ,img_binary)

cv.imshow("Binary", img_binary)
cv.waitKey(0)
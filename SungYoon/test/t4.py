import cv2 as cv


img_color = cv.imread('./img/test.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)


height,width = img_binary.shape[:2]

f = open('image.txt', 'w')

for y in range(height):
    for x in range(width):
        print("%3d"%img_binary[y,x], end=" ")
        f.write("%3d " % img_binary[y,x])
    print("")
    f.write("\n")

f.close()
cv.imshow("Binary", img_binary)
cv.waitKey(0)
import matplotlib.pyplot as plt

import cv2

def draw_image(original_img, result_img, title, sub_title1, sub_title2):

    fig = plt.figure()

    fig.suptitle(title)

    ax = fig.add_subplot(1, 2, 1)

    ax.imshow(original_img, cmap=plt.cm.gray)

    ax.set_title(sub_title1)

    ax = fig.add_subplot(1, 2, 2)

    ax.imshow(result_img, cmap=plt.cm.gray)

    ax.set_title(sub_title2)

    plt.show()

def set_watermark():

    camera_img_path = "./img/camera.bmp"

    zero_img_path = "./img/zero.bmp"

    camera_img = cv2.imread(camera_img_path, cv2.IMREAD_GRAYSCALE)

    zero_img = cv2.imread(zero_img_path, cv2.IMREAD_GRAYSCALE)

    out_img = camera_img.copy()

    row, col = camera_img.shape

    for i in range(0, row):

        for j in range(0, col):

            if zero_img[i, j] == 0:

                out_img[i, j] = camera_img[i, j] & 254

            else:

                out_img[i, j] = camera_img[i, j] | 1

    draw_image(camera_img, out_img, "Set Watermark", "Original Image", "Result Image")

    cv2.imwrite("camera_watermark.bmp", out_img)

set_watermark()
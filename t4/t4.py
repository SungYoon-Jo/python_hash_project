import matplotlib.pyplot as plt
import cv2

def draw_image(original_img, out_list, title, sub_title1):
    fig = plt.figure()
    fig.suptitle(title)
    
    ax = fig.add_subplot(3,5,6)
    ax.imshow(original_img, cmap=plt.cm.gray)
    ax.set_title(sub_title1)
    
    ax = fig.add_subplot(3,5,2)
    ax.imshow(out_list[0], cmap=plt.cm.gray)
    ax.set_title("Bit8")
    
    ax = fig.add_subplot(3,5,3)
    ax.imshow(out_list[1], cmap=plt.cm.gray)
    ax.set_title("Bit7")
    
    ax = fig.add_subplot(3,5,4)
    ax.imshow(out_list[2], cmap=plt.cm.gray)
    ax.set_title("Bit6")
    
    ax = fig.add_subplot(3,5,5)
    ax.imshow(out_list[3], cmap=plt.cm.gray)
    ax.set_title("Bit5")
    
    ax = fig.add_subplot(3,5,12)
    ax.imshow(out_list[4], cmap=plt.cm.gray)
    ax.set_title("Bit4")
    
    ax = fig.add_subplot(3,5,13)
    ax.imshow(out_list[5], cmap=plt.cm.gray)
    ax.set_title("Bit3")
    
    ax = fig.add_subplot(3,5,14)
    ax.imshow(out_list[6], cmap=plt.cm.gray)
    ax.set_title("Bit2")
    
    ax = fig.add_subplot(3,5,15)
    ax.imshow(out_list[7], cmap=plt.cm.gray)
    ax.set_title("Bit1")
    
    plt.show()
    
def do_bit_plane_slicing():
    file_path = "./img/camera.bmp"
    
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    
    out_img1 = img.copy()
    out_img2 = img.copy()
    out_img3 = img.copy()
    out_img4 = img.copy()
    out_img5 = img.copy()
    out_img6 = img.copy()
    out_img7 = img.copy()
    out_img8 = img.copy()
    
    row, col = img.shape
    
    for i in range(0, row):
        for j in range(0, col):
            out_img1[i, j] = 255 if (img[i,j] & (1 << 7)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 6)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 5)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 4)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 3)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 2)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 1)) else 0 
            out_img1[i, j] = 255 if (img[i,j] & (1 << 0)) else 0 
            
            
            
    out_list = [out_img1, out_img2, out_img3, out_img4, out_img5, out_img6, out_img7, out_img8]
    
    cv2.imwrite("bit8_slicing.bmp", out_img1)
    draw_image(img, out_list, "Bit Plane Slicing", "Original Image")

do_bit_plane_slicing()
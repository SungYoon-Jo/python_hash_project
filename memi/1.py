import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
img = mpimg.imread("./memi.jpg")
print(img)

image_plot = plt.imshow(img)
plt.show()


""" 
- matplotlib image display
- understanding the finer contents of an image
- image manipulation
    - copy and pasting parts of the image
    - change contents on the image with pixel change
- opencv key interfaces 
"""

import cv2
from random import randint
from matplotlib import pyplot as plt

img = cv2.imread('assets/fruitbasket.jpg')


# displaying an image with matplotib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') 
# cmap,          maps data values to colors
# "gray"    - greyscale
# "viridis" - viridis (default colormap)
# interpolation, controls how pixels are resampled when zooming/display in different size/shapes
# "bicubic" - higher quality than bilinear
# "spline"/"lanczos" - even higher quality
plt.xticks([]), plt.yticks([])  # hides the x and y axis
plt.show()

print(img)
# outputs numpy arrays of pixel colour schemes,
# standard is R,G,B, OpenCV uses B,G,R

print(img.shape)
# outputs (height,width,channels(3 for rgb, 2 for b&w))

# looking at the [first row][nth pixel:to the mth pixel]
print(img[0][25:40])

# looking at one pixel
print(img[0][30])


for i in range(100): # look through the first 100 rows
    # shape gives you modification of pixel [rows,columns,channels]
    for j in range(img.shape[1]): # the entrire column
        img[i][j] = [randint(0,255),
                     randint(0,255),
                     randint(0,255)]

# copying and pasting a part of the image 
# the copy dimensions has to be the same with the paste dimensions
tag = img[300:500,600:900]
img[200:400,750:1050] = tag
cv2.imshow('Image',img)

# waits for an input key
key = cv2.waitKey(0)
if key == 27: # esc key in ascii
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('assets/fruitbasketrandom.jpg',img)
    cv2.destroyAllWindows()



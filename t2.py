import cv2
import random

img = cv2.imread('assets/fruitbasket.jpg')

# print(img)
# outputs numpy arrays of pixel colour schemes,
# standard is R,G,B, OpenCV uses B,G,R

# print(img.shape)
# outputs (height,width,channels(3 for rgb, 2 for b&w))

# looking at the [first row][nth pixel:to the mth pixel]
# print(img[0][25:40])
# looking at one pixel
# print(img[0][30])




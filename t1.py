import cv2 

# -1, cv2.IMREAD_COLOR:    Loads a color image, any transparency of the image will be neglected. Default flag
# 0, cv2.IMREAD_GRAYSCALE: loads image in greyscale
# 1, cv2.IMREAD_UNCHANGED: loads image as such including alpha channel
img =cv2.imread('assets/fruitbasket.jpg')

# resizes image in dimensions of pixels, 400 by 400 pixels
img = cv2.resize(img,(400,400))
# resizes image based on itself, 
# fx=0.5 halves its length, 
# fy=0.5 halves its height
img = cv2.resize(img,(0,0),fx=2,fy=2)
# rotates image with angle
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

# creates a new image with the manipulations
cv2.imwrite('assets/new_img.jpg',img)

cv2.imshow('Image',img) # label of window, image to show
cv2.waitKey(0)          # wait infinitly, any key will be detected for x secs, if this line is done, next line
cv2.destroyAllWindows() # closes all windows
'''
template matching, used to find and locate a template in an image, for finding objectsin an image
stores functions in a tuple and using a loop to apply each method

'''

import matplotlib.pyplot as plt
import numpy as np
import cv2

'''image options
sources:
rsaf1.png
rsaf2.png

templates:
rsaf1_jet1.png
rsaf2_jet1.png
'''

# loads image and template as grayscale
img = cv2.resize(cv2.imread('assets/rsaf2.png', 0),(0,0),fx=0.4,fy=0.4)
template = cv2.resize(cv2.imread('assets/rsaf1_jet1.png', 0),(0,0),fx=0.4,fy=0.4)

if img is None or template is None:
    print("Error: Could not load images.")
    exit()

img = cv2.resize(img,(0,0),fx=0.4,fy=0.4)
template = cv2.resize(template,(0,0),fx=0.4,fy=0.4)

h,w = template.shape

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED
]


for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2,template,method)

    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result) # returns th min and max values and their locations in the result matrix
    print(min_val,max_val,min_loc,max_loc)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR]:     # for these methods, the min value is the best match, max values are better for other methods
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h) # bottom right corner of rectangle to be drawn around the matched template
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow('match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
harris method corner detection
'''
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os 

def harriscorner():
    root = os.getcwd() # current working directory
    imgPath = os.path.join(root,'assets/checkersboard.png') # image path
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgGray = np.float32(imgGray)

    plt.figure()
    plt.subplot(131) # 131 means 1 row, 3 columns, first plot
    plt.imshow(imgGray, cmap='gray') # cmap gray for grayscale image

    plt.savefig
    plt.subplot(132) # 132 means 1 row, 3 columns, second plot
    
    blockSize = 5 # size of neighbourhood, a square window used to compare pixels
    sobelSize = 3 # aperture parameter for the Sobel operator
    k = 0.04      # Harris detector free parameter in the equation
    # sensiticvity parameter that affects the thresholding step
    
    '''
    det(m) = lambda1*lambda2 (product of eigenvalues)
    trace(m) = lambda1 + lambda2 (sum of eigenvalues)
    Harris response:
    R = det(m) - k*(trace(m))^2
    If both eigenvalues are large, R is large positive -> corner
    '''

    # Harris corner detection
    # cv.cornerHarris(source image, block size, sobel size, k)
    harris = cv.cornerHarris(imgGray,blockSize,sobelSize,k)
    plt.imshow(harris)
    plt.title('Harris Response Map')
    plt.subplot(133)

    # 0.05, adjustable, threshold value determines likelihood of a pixel is a corner
    # higher threshold = stricter corner detection -> fewer corners detected
    threshold = np.percentile(harris, 65) # 65th percentile, top 35% of values are considered corners, hand adjusted
    mask = harris>threshold*harris.max() # a mask of corners
    # imgRGB[mask] = [255,0,0] # marks corners in red

    coords = np.where(mask) # get coordinates of corners
    for (x,y) in zip(*coords):
        imgRGB = cv.circle(imgRGB,(y,x),2,(0,255,0),1) # mark corners with green circles
    
        # Print some statistics
    print(f"Harris response min: {harris.min():.2f}, max: {harris.max():.2f}")
    print(f"Number of corners detected: {len(coords[0])}")
    print(f"Threshold value used: {threshold:.2f}")

    plt.imshow(imgRGB)
    plt.title('Corners Detected Circled')

    plt.show()

    # Print some statistics
    print(f"Harris response min: {harris.min():.2f}, max: {harris.max():.2f}")
    print(f"Number of corners detected: {len(zip(x,y)[0])}")
    print(f"Threshold value used: {threshold:.2f}")
    
if __name__ == '__main__':
    harriscorner()
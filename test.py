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
    imgGrayFloat = np.float32(imgGray)

    plt.figure(figsize=(15,5))
    
    # First plot: Grayscale image
    plt.subplot(131) # 131 means 1 row, 3 columns, first plot
    plt.imshow(imgGray, cmap='gray') # cmap gray for grayscale image
    plt.title('Grayscale Image')
    plt.axis('off')
    
    # Second plot: Harris response
    plt.subplot(132) # 132 means 1 row, 3 columns, second plot
    blockSize = 5 # size of neighbourhood, a square window used to calculate the derivative covariation matrix 
    sobelSize = 3 # aperture parameter, gradient precision
    k = 0.9       # Harris detector free parameter in the equation
     
    # Harris corner detection
    # cv.cornerHarris( source image, block size, sobel size, k)
    harris = cv.cornerHarris(imgGrayFloat,blockSize,sobelSize,k)
    # returns a 2D array of scores that represent the confidence of corners at each pixel location

    plt.imshow(harris, cmap='hot') # cmap = hot, heatmap style
    plt.title('Harris Response Map')
    plt.colorbar()
    plt.axis('off')
    
    # Third plot: Original image with circled corners
    plt.subplot(133)
    
    # Create a copy to draw on
    imgWithCorners = imgRGB.copy()
    
    # Normalize Harris response to 0-255 range for better thresholding

    harris_norm = cv.normalize(harris, None, 0, 255, cv.NORM_MINMAX, cv.CV_32FC1)

    # Threshold to find corners (adjust threshold value as needed)
    threshold = 0.01  # 5% of max value
    thresh_value = threshold * harris_norm.max()
    
    # Find corner coordinates
    corner_coords = np.where(harris_norm > thresh_value)
    print(corner_coords)
    
    # Draw circles at corner positions
    for y, x in zip(*corner_coords):
        cv.circle(imgWithCorners, (x, y), 5, (0, 255, 0), 2)  # Green circles
    
    # Alternative: Mark corners with red pixels (original method)
    # imgWithCorners[harris_norm > thresh_value] = [255, 0, 0]  # Red pixels
    
    plt.imshow(imgWithCorners)
    plt.title(f'Detected Corners (threshold={threshold})')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Print some statistics
    print(f"Harris response min: {harris.min():.2f}, max: {harris.max():.2f}")
    print(f"Number of corners detected: {len(corner_coords[0])}")
    print(f"Threshold value used: {thresh_value:.2f}")

if __name__ == '__main__':
    harriscorner()
'''
template matching, used to find and locate a template in an image, for finding objectsin an image
using dictionary to store the different methods of template matching and using a loop to apply each method
iterates through the dictionary and applies each method as well as display the results on a subplot
finds the min and max values and their locations in the result matrix

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
    
h,w = template.shape

methods = {
    'TM_CCOEFF': cv2.TM_CCOEFF,
    'TM_CCOEFF_NORMED': cv2.TM_CCOEFF_NORMED,
    'TM_CCORR': cv2.TM_CCORR,
    'TM_CCORR_NORMED': cv2.TM_CCORR_NORMED,
    'TM_SQDIFF': cv2.TM_SQDIFF,
    'TM_SQDIFF_NORMED': cv2.TM_SQDIFF_NORMED
}

# Determine grid size for subplots
n_methods = len(methods)
cols = 3
rows = (n_methods + cols - 1) // cols

plt.figure(figsize=(15, 10))

# enumerate(), adds a counter to an iterable and returns it as an enumerate object, 
# can be used in a loop to get the index and the value of the iterable at the same time

for i, (name, method) in enumerate(methods.items(), 1):
    # Apply template matching
    result = cv2.matchTemplate(img, template, method)
    
    # Normalize result to 0-255 for display (as heatmap)
    norm_result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
    norm_result = np.uint8(norm_result)
    
    # Apply colormap (OpenCV's JET)
    heatmap = cv2.applyColorMap(norm_result, cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)  # Convert for matplotlib
    
    # Find best match location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Choose location based on method type
    if name in ['TM_SQDIFF', 'TM_SQDIFF_NORMED', 'TM_CCORR']:
        top_left = min_loc
        best_val = min_val
        color = 'blue'   # lower is better
    else:
        top_left = max_loc
        best_val = max_val
        color = 'red'    # higher is better
    
    # Draw a marker on the heatmap at the best location
    # The heatmap size is smaller, so we use top_left directly (it's in result coordinates)
    cv2.drawMarker(heatmap, top_left, (255,255,255), markerType=cv2.MARKER_CROSS, 
                   markerSize=10, thickness=2)
    
    # Add subplot
    plt.subplot(rows, cols, i)
    plt.imshow(heatmap)
    plt.title(f'{name}\nBest value: {best_val:.3f}', color=color)
    plt.axis('off')

plt.tight_layout()
plt.show()

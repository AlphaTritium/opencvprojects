'''
harris method corner detection
non maximal suppression       : only keep local maxima as corners, suppress non-maximal responses in the neighborhood
normalisation                 : min-max applied

image input -> grayscale -> NMS dialation (better than none)-> harris corner detection -> mark and circle -> output

'''
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os              # library for operation system interaction works on major operating systems, a portability wrapper

def nms(source, threshold):
    '''
    non-maximum suppression algorithm

    :param source: image to be iterated
    :param threshold: strictness of corner detection
    '''

    # Create a copy of the Harris response to modify
    nms_response = np.zeros_like(source)
    
    # Get the dimensions of the Harris response
    rows, cols = source.shape
    
    # Iterate through each pixel in the Harris response
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Check if the current pixel is a local maximum and above the threshold
            if source[i, j] > threshold and source[i, j] == np.max(source[i-1:i+2, j-1:j+2]):
                nms_response[i, j] = source[i, j]
    
    return nms_response

def min_max_normalise(arr,new_min=0,new_max=1,dtype=np.float32):
    '''
    normalise color image using global min/max across all channels
    perform min-max normalisation on a numpy array

    parameters:
        arr (np.ndarray): input array
        new_min (float): desired min output range
        new_max (float): max output range
        dtype (np.dtype): data type output array

    returns:
        np.ndarray: normalised array with values in [new_min, new_max]
    '''
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.full_like(arr, (new_min + new_max)/2)

    # apply normalisation formula
    # first scale to [0,1], then to [new_min,new_max], then convert to desired dtype
    # Vectorized formula (elements are calculated simultaneously)
    scaled = (arr - min_val) / (max_val - min_val)          # [0, 1]
    result = scaled * (new_max - new_min) + new_min         # [new_min, new_max]

    return result.astype(dtype)
    
def grayscale_min_max_loops(arr, new_min=0, new_max=1, dtype=np.float32):
    '''
    Docstring for grayscale_min_max_loops
    
    :param arr: image array (height, width, channels)
    :param new_min: desired min output range
    :param new_max: desired max output range
    :param dtype: desired datatype output
    :rtype: NDArray[floating[_32Bit]]
    
    '''
        
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.full_like(arr, (new_min + new_max) / 2, dtype=dtype)

    # Prepare output array of correct shape and dtype
    result = np.empty_like(arr, dtype=dtype)

    for i in range(arr.shape[0]):          # each row
        for j in range(arr.shape[1]):      # each column
            # Correct formula
            norm_val = (arr[i, j] - min_val) / (max_val - min_val)
            norm_val = norm_val * (new_max - new_min) + new_min
            result[i, j] = norm_val

    return result
    
def per_channel_normalize(arr, new_min=0, new_max=1, dtype=np.float32):
    '''
    per_channel_normalize
    
    :param arr: image array (height, width, channels)
    :param new_min: desired min output range
    :param new_max: desired max output range
    :param dtype: desired datatype output
    '''

    # Compute min and max over the spatial dimensions (height, width)
    # Keepdims=True so the result can broadcast back to the original shape
    min_vals = np.min(arr, axis=(0, 1), keepdims=True)
    max_vals = np.max(arr, axis=(0, 1), keepdims=True)

    # Handle constant channels
    range_vals = max_vals - min_vals
    # if range is zero, avoid division by zero; set those channels to new_min later
    # for simplicity, we'll do a mask or use np.divide with where= condition

    # Create an output array
    result = np.empty_like(arr, dtype=np.float64)

    # For each channel, perform normalisation only if range > 0
    for c in range(arr.shape[2]): 
        # iterate over channels
        if range_vals[0,0,c] == 0: 
            # if all values in the channel are the same, set to midpoint of new range
            result[:,:,c] = (new_min + new_max) / 2
        else: 
            # normalise this channel
            scaled = (arr[:,:,c] - min_vals[0,0,c]) / range_vals[0,0,c]
            result[:,:,c] = scaled * (new_max - new_min) + new_min

    return result.astype(dtype)

def harris_response():
    pass

def harriscorner():
    '''
    harris response corner detection strategy
    '''

    root = os.getcwd() # current working directory
    imgPath = os.path.join(root,'assets/checkersboard.png') # image path
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgGray = np.float32(imgGray)
    
    blockSize = 5 # size of neighbourhood, a square window used to compare pixels
    sobelSize = 3 # aperture parameter for the Sobel operator
    k = 0.04      # Harris detector free parameter in the equation
    # sensitivity parameter that affects the thresholding step

    '''
    det(m) = lambda1*lambda2 (product of eigenvalues)
    trace(m) = lambda1 + lambda2 (sum of eigenvalues)
    Harris response:
    R = det(m) - k*(trace(m))^2
    If both eigenvalues are large, R is large positive -> corner
    '''

    # Harris corner detection
    # cv.cornerHarris(source image, block size, sobel size, k)
    harris_raw = cv.cornerHarris(imgGray,blockSize,sobelSize,k)

    # 0.05, adjustable, threshold value determines likelihood of a pixel is a corner
    # higher threshold = stricter corner detection -> fewer corners detected
    threshold = np.percentile(harris_raw, 65) # 65th percentile, top 35% of values are considered corners, hand adjusted

    dialated = nms(np.int32(harris_raw), threshold*harris_raw.max()) # apply non-maximal suppression with a threshold

    # a mask of corners, boolean array where True indicates a corner
    mask_threshold = harris_raw>threshold*harris_raw.max() 

    corners_nms = dialated>threshold*harris_raw.max() 

    # imgRGB[mask] = [255,0,0] # marks corners in red

    coords = np.where(mask_threshold) # get coordinates of corners
    for (x,y) in zip(*coords):
        img_with_corners = cv.circle(imgRGB,(y,x),2,(0,255,0),1) # mark corners with green circles
    
    # Print some statistics
    print(f"Harris response min: {harris_raw.min():.2f}, max: {harris_raw.max():.2f}")
    print(f"Number of corners detected: {len(coords[0])}")
    print(f"Threshold value used: {threshold:.2f}")

    # After computing all images and masks, create a 2x3 grid
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes_flat = axes.flat  # flatten to 1D array for easy iteration

    harris_norm = min_max_normalise(harris_raw) # normalised harris response for better visualization

    # Define each plot as a dictionary
    plots = [
        {"img": imgGray,          "title":  "1. Grayscale Input",                            "cmap": "gray", "colorbar": False},
        {"img": harris_raw,       "title":  "2. Raw Harris Response",                        "cmap": "hot", "colorbar": True},
        {"img": harris_norm,      "title":  "3. Normalized Harris",                          "cmap": "hot", "colorbar": True},
        {"img": mask_threshold,   "title": f"4. Threshold Mask\n(>{threshold:.2f})",         "cmap": "gray", "colorbar": False},
        {"img": corners_nms,      "title":  "5. After NMS",                                  "cmap": "gray", "colorbar": True},
        {"img": img_with_corners, "title": f"6. Detected Corners\n{len(coords[0])} points",  "cmap": None, "colorbar": False},
    ]

    # Iterate and plot
    for ax, plot in zip(axes_flat, plots):
        if plot["cmap"] is None:
            ax.imshow(plot["img"])
        else:
            im = ax.imshow(plot["img"], cmap=plot["cmap"])
            if plot["colorbar"]:
                plt.colorbar(im, ax=ax)
        ax.set_title(plot["title"])
        ax.axis("off")

    plt.tight_layout()
    plt.show()
    


harriscorner()


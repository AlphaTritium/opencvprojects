'''
- video processing
- video replication and orientation manipulation
- simple error detection
- clean up
- be aware of dimensions when frame manipulations
'''
import numpy as np
import cv2

# video capture
# cap = cv2.VideoCapture(0) 0 for 1 source, 1 for another source, and 2 for another and so on
# cap = cv2.VideoCapture("video.mp4")     file name instead
cap = cv2.VideoCapture(0) 

while True:
    
    # attempts to read another frame
    # ret   - boolean, true for sucessful capture of frame, false for failure
    # frame - an image array
    ret, frame = cap.read()
    width = int(cap.get(3)) # 3 - width property identifier
    height = int(cap.get(4)) # 4 - height property identifier, 17 identifier

    # mirroring videos by copy and pasting image arrays
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2,:width//2] = smaller_frame # paste int on the top left
    image[height//2:,:width//2] = smaller_frame # bottom left
    image[:height//2,width//2:] = smaller_frame # top right
    image[height//2:,width//2:] = smaller_frame # bottom right
    # creates a window with 4 feeds each taking one corner

    # error detection
    if not ret:
        print("Failed to grab frame")
        break

    # displays frame
    cv2.imshow('frame',image)

    # exit code
    if cv2.waitKey(1) == ord('q'): # waits 1 ms for key 'q' which ends frame capturing
        break

# cleanup
cap.release()
cv2.destroyAllWindows()

'''
image[:height//2,:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE) # paste int on the top left
ValueError: could not broadcast input array from shape (320,240,3) into shape (240,320,3)
when rotating a rectangular feed, the width and height interchange
when you change the frame dimensions, you cant put it back into the original slot because it doesnt fit.
'''
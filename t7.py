'''
corner detection 
cv2.goodFeaturesToTrack() 
Shi-Tomasi corner detection algorithm
'''

import numpy as np
import cv2

file = cv2.imread('assets/eva1.png')
file = cv2.resize(file,(0,0),fx=0.5,fy=0.5)
gray = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)

# cv2.goodFeaturesToTrack(source,quantity,quality,min euclidean distance)
# euclidean distance, points (x1,y1),(x2,y2)
# sqrt((x2-x1)^2+(y2-y1)^2)
corners = cv2.goodFeaturesToTrack(gray,250,0.01,5)
# print(corners) # coordinates
corners = np.int32(corners)
print(corners) # coordinates in int32

for corner in corners:
    x, y = corner.ravel() # flattens an array [[x,y]] -> [x,y]
    cv2.circle(file,(x,y),5,(0,0,255),1)

# connect the corners with lines if they are close to each other
for i in range(len(corners)): # iterate through all the corners
    for j in range(i+1,len(corners)): # iterate through all the corners except the ones already iterated (i+1)
        
        '''
        corner1 = tuple(corners[i][0]) 
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x:int(x),np.random.randint(0,255,3))) # random color for each line
        cv2.line(file,corner1, corner2,color,1) # draw a line between the two corners with the random color
        '''

        # ravel() flattens the array [[x,y]] -> [x,y]
        # connects the corners with lines if they are close to each other (distance < 20)
        x1,y1 = corners[i].ravel()
        x2,y2 = corners[j].ravel()
        dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
        if dist < 20:
            cv2.line(file,(x1,y1),(x2,y2),(255,0,0),1)
        

cv2.imshow('frame',file)
cv2.waitKey(0)
cv2.destroyAllWindows()

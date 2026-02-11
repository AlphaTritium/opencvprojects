import numpy as np
import cv2

file = cv2.imread('assets/fruitbasket.jpg')
file = cv2.resize(file,(0,0),fx=0.5,fy=0.5)
gray = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)

# cv2.goodFeaturesToTrack(source,quantity,quality,min euclidean distance)
# euclidean distance, points (x1,y1),(x2,y2)
# sqrt((x2-x1)^2+(y2-y1)^2)
corners = cv2.goodFeaturesToTrack(gray,250,0.01,5)
# print(corners) # coordinates
corners = np.int32(corners)


for corners in corners:
    x, y = corners.ravel() # flattens an array [[x,y]] -> [x,y]
    cv2.circle(file,(x,y),5,(0,0,255),1)



cv2.imshow('frame',file)
cv2.waitKey(0)
cv2.destroyAllWindows()

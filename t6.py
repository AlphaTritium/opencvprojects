'''
- shape creation
    - polygon
    - ellipses
- mouse as a paint brush
'''
import numpy as np
import cv2

file = cv2.VideoCapture(0)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # triggers when mouse double clicks
        cv2.circle(canvas,(x,y),100,(255,0,0),-1)

# creates a black image, a window and binf the function to window
canvas = np.ones((512,512,3),np.uint8)*255
cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas',draw_circle)

while True:
    ret, frame = file.read()
    width = int(file.get(3))
    height = int(file.get(4))

    # drawing a neon green line on feed from (0,0) to bottom right with thickness of 5 px
    img = cv2.line(frame, (0,0),(width,height),(40,255,0),5)
    
    # (source,shape centre,width,height,0,0,degrees, start angle, end angle,fill or line thickness)
    img = cv2.ellipse(img, (250,250),(100,150),0,0,270,150,-1)
    
    # plotting points of a polygon
    pts = np.array([[200,150],[75,50],[150,40],[30,30],[175,175]],np.int32)
    # np.reshape((ROWS,1,2)
    pts = pts.reshape(-1,1,2) # required for polylines, fill poly
    # cv2.polylines(source, points, closed shape or not, line color)
    img = cv2.polylines(img, [pts],True, (255,255,0))

    cv2.imshow('canvas',canvas)
    cv2.imshow('frame',img)

    if not ret:
        print("failed to grab frame")
        break

    if cv2.waitKey(1) == ord('q'):
        break

file.release()
cv2.destroyAllWindows()

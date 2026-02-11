
'''
- draw lines, cricles, rectangles and add texts on image/video
- 
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # cv2.line(source image,starting point, ending point, color, line thickness)
    img = cv2.line(frame, (0,0),(width,height),(255,0,0),5)
    img = cv2.line(img, (0,height),(width,0),(0,255,0),5)
   
    # cv2.rectangle(source image, centre position, radius, colour, line thickness)
    img = cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)
  
    # cv2.circle(source image, certre position, radius, color, line thickness)
    img = cv2.circle(img, (300,300),60, (0,0,255), -1)
   
    # when line thickness = -1, fills up shape
    font = cv2.FONT_HERSHEY_SIMPLEX
   
    # cv2.line(image source, centre position, font, font scale, color, line thickness, line type)
    img = cv2.putText(img, "I am Great!", (10,height-10), font, 1,  (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
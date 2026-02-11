'''
- circle and recatngle paint
- save function
- mouse events

'''
import cv2
import numpy as np
'''
lists all mouse events available  
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
'''

drawing = False
mode = True
ix,iy = -1,-1 # default cursor location

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing == True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(canvas,(ix,iy),(x,y),(0,255,0),1)
            else:
                cv2.circle(canvas,(x,y),5,(0,0,255),1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(canvas,(ix,iy),(x,y),(0,255,0),1)
        else:            
            cv2.circle(canvas,(x,y),5,(0,0,255),1)

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas',draw_circle)
canvas = np.ones((512,512,3),np.uint8)*255

while True:
    cv2.imshow('canvas',canvas)
    if cv2.waitKey(1) == ord('m'):
        mode = not mode

    elif cv2.waitKey(1) == ord('s'):
        name = str(input('name of image: '))
        cv2.imwrite(f'assets/{name}.jpg',canvas)

    elif cv2.waitKey(1) == 27: # esc buttom
        break

cv2.destroyAllWindows()
    
'''
face and eye detection
haar cascades, pretrained claassifier for object detection

face has a higher prioty than eye since there must be an eye inside a face
the strategy is to detect and highlight the face first, then  crop the face region region of interest
then apply eye detectection to the face region
avoids false positives and reduces redundant searches


'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# haar cascades are XML files that contain the data for the classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()

    # converts image to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    '''
    detects faces in the image, returns a list of rectangles around the faces, 1.3 is the scale factor, 5 is the minNeighbors 
    minNeighbors, the number of neighbors each candidate rectangle should have to retain it, higher value results in less detections but with higher quality
    scaleFactor, the parameter specifying how much the image size is reduced at each image scale, used to create the scale pyramid
    for example, 1.3 means the image is reduced by 30% a each scale
    '''

    # haar cascade works by sliding a window across the image and applying the classifier to each window, 
    # does this at multiple scales to detect objects of different sizes, 
    # the classifier is a decision tree that uses the features in the XML file to classify the window as containing the object or not
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

    print(faces)
    # list of rectangles around the faces
    # each rectangle is represented as (x, y, w, h)
    # where (x, y) is the top-left corner of the rectangle, and w and h are the width and height of the rectangle respectively

    # detects faces first
    for (x,y,w,h) in faces:

        # highlighting the face with a rectangle
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)

        # cropping the face region from the grayscale image and the color image
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # applies eye detection to the face region, returns a list of rectangles around the eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

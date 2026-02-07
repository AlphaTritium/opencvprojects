import numpy as np
import cv2

# videocam stores video source
videocam = cv2.VideoCapture(0)
img = cv2.imread('assets/fruitbasket.jpg')

# Store the current operation state (initialize with original frame)
current_operation = 'w'  # 'w' means original frame
ret, frame = videocam.read()
width = int(videocam.get(3))
height = int(videocam.get(4))
resized = cv2.resize(img, (width, height))

print('key operations: ','\n',
'n - not','\n',
'o - or','\n',
'a - and','\n',
'r - nor','\n',
'x - xor','\n',
'w - original','\n',
'm - mask','\n',
'q - quit','\n',
'')

while True:
    # gets frame and status from the source
    ret, frame = videocam.read()
    if not ret:
        break
    
    # H-Hue, color type, 0-179
    # S-Saturation, colour diversity, 0-255
    # V-value, brightness, 0-255
    # converting frame colour contents to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # displays white if the color detected is within color range 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Check for key press to change operation mode
    key = cv2.waitKey(1) & 0xFF
    
    # Update current operation based on key press
    if key == ord('n'):
        current_operation = 'n'  # bitwise NOT
    elif key == ord('o'):
        current_operation = 'o'  # bitwise OR
    elif key == ord('a'):
        current_operation = 'a'  # bitwise AND
    elif key == ord('r'):
        current_operation = 'r'  # bitwise NOR (NOT of OR)
    elif key == ord('x'):
        current_operation = 'x'  # bitwise XOR
    elif key == ord('w'):
        current_operation = 'w'  # original frame
    elif key == ord('m'):
        current_operation = 'm'  # mask display
    elif key == ord('q'):
        break  # quit application
    
    # Apply the current operation (persists until changed)
    if current_operation == 'n':
        final = cv2.bitwise_not(frame)
    elif current_operation == 'o':
        final = cv2.bitwise_or(frame, resized)
    elif current_operation == 'a':
        final = cv2.bitwise_and(frame, resized)
    elif current_operation == 'r':
        # NOR = NOT(OR) - OpenCV doesn't have direct bitwise_nor
        or_result = cv2.bitwise_or(frame, resized)
        final = cv2.bitwise_not(or_result)
    elif current_operation == 'x':
        final = cv2.bitwise_xor(frame, resized)
    elif current_operation == 'w':
        final = frame  # original frame
    elif current_operation == 'm':
        # since normal display doesnt work
        # because of greyscale
        # must convert 1-channel mask back to 3-channel BGR for text display
        # still black and white(greyscale) for the rest of the display
        final = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    else:
        final = frame  # default to original
    
    # cv2.bitwise_and, cv2.bitwise_or, cv2.bitwise_nor, cv2.bitwise_xor
    # be mindful of the dimensions - both sources must have same dimensions
    # function(source1, source2)
    
    # Display the current operation mode on the frame
    cv2.putText(final, f"Mode: {current_operation}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(final, "Press keys: n,o,a,r,x,w,m,q", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('frame', final)

# Release resources
videocam.release()
cv2.destroyAllWindows()
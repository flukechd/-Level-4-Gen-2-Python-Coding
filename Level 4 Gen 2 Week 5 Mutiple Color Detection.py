import cv2
import numpy as np

# Start the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of blue color in HSV
    blue_lower = np.array([99,115,150])
    blue_upper = np.array([110, 255, 255])
    
    # Define the range of red color in HSV
    red_lower = np.array([136, 87, 110])
    red_upper= np.array([180, 255, 255])
    
    # Create the blue and green masks
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    # Combine the masks
    mask = cv2.bitwise_xor(blue_mask, red_mask)
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Show the results
    cv2.imshow('MUTICOLOR DETECTION', result)
    cv2.waitKey(1)
    
    #---------------------------------------------------------------------------------------
    # # Find the contours in the resulting image
    # contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # # Draw the contours on the original image
    # cv2.drawContours(frame, contours, -1, (255, 51, 153), 3)
    
    # # Draw the contours on the original image
    # for i in range(len(contours)):
    #     if cv2.contourArea(contours[i]) > 500:  # add a condition to filter out small contours
    #         if cv2.mean(hsv, mask=mask)[0] < 60:  # change the color to green if the detected color is green
    #             cv2.drawContours(frame, contours, i, (0, 255, 0), 4)
    #         else:  # change the color to blue if the detected color is blue
    #             cv2.drawContours(frame, contours, i, (255, 0, 0), 4)
                
    # Show the results
    # cv2.imshow('MUTICOLOR DETECTION', frame)
    # cv2.waitKey(1)

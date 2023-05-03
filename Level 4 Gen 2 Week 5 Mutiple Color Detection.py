import cv2

# Start the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()

    # Convert the frame to the HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors to detect
    lower_red = (136, 87, 111)
    upper_red = (180, 255, 255)
    lower_blue = (99,115,150)
    upper_blue = (110,255,255)

    # Create masks for the frame using the lower and upper bounds of the red and blue colors
    red_mask = cv2.inRange(frame_hsv, lower_red, upper_red)
    blue_mask = cv2.inRange(frame_hsv, lower_blue, upper_blue)

    # Apply the masks to the frame
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Show the results
    cv2.imshow("Red Result", red_result)
    cv2.imshow("Blue Result", blue_result)
    cv2.waitKey(1)

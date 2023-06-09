import cv2

# Start the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()

    # Convert the frame to the HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors to detect
    lower = (136, 87, 111)
    upper = (180, 255, 255)
    # Create a mask for the frame using the lower and upper bounds of the red color
    mask = cv2.inRange(frame_hsv, lower, upper)

    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the result
    cv2.imshow("Result", result)
    cv2.waitKey(1)
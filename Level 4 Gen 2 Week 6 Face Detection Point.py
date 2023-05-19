import cv2
import mediapipe as mp
import matplotlib.pyplot as plt


# Initialize the mediapipe face detection class.
mp_face_detection = mp.solutions.face_detection

# Setup the face detection function.
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

# Initialize the mediapipe drawing class.
mp_drawing = mp.solutions.drawing_utils

# Specify the video capture source (usually 0 for the default webcam).
video_capture = cv2.VideoCapture(0)
video_capture.set(3,1280)
video_capture.set(4,960)

# Continuously process frames from the webcam feed.
while True:
    # Read a frame from the video capture source.
    ret, frame = video_capture.read()

    # Check if the frame was successfully captured.
    if not ret:
        break

    # Perform face detection on the frame.
    face_detection_results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Create a copy of the frame to draw the bounding box and key points.
    img_copy = frame.copy()

    # Check if any face(s) were detected.
    if face_detection_results.detections:
        # Iterate over the detected faces.
        for face_no, face in enumerate(face_detection_results.detections):
            # Draw the face bounding box and key points on the copy of the frame.
            mp_drawing.draw_detection(image=img_copy, detection=face,
                                       keypoint_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0),
                                                                                     thickness=2,
                                                                                     circle_radius=2))

    # Display the resultant frame with the bounding box and key points drawn.
    cv2.imshow('Face Detection', img_copy)

    # Exit the loop if 'q' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture source and close all windows.
video_capture.release()
cv2.destroyAllWindows()
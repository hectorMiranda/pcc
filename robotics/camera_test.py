import cv2

# Initialize the capture object.
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Capture a frame.
ret, frame = cap.read()
if ret:
    # Display the frame to see if it's black.
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # If the frame shows correctly, the issue might be elsewhere.
else:
    print("Failed to capture frame")

cap.release()

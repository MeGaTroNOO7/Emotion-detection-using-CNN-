import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
else:
    # Read and display frames from the camera
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow("Camera", frame)

        
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
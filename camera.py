import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Check camera connection")
else:
    # Read and display frames from the camera
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to read camera port")
            break

        cv2.imshow("Camera", frame)

        
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
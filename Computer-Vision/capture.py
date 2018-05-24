import cv2


# Capture from camera
video = cv2.VideoCapture(-1)

while True:
    check, frame = video.read()
    # Show live images
    cv2.imshow("Capturing", frame)
    # Refresh every .5 sec
    key = cv2.waitKey(1)
    # Break loop
    if key == ord('q'):
        break

# Close camera
video.release()
cv2.destroyAllWindows()

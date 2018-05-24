import cv2


# Capture from camera
video = cv2.VideoCapture(-1)

while True:
    check, frame = video.read()
    # Show live images
    cv2.imshow("Capturing", frame)
    # Refresh every 1 msec
    key = cv2.waitKey(1)
    # Break loop
    if key == ord('q'):
        break

# Close camera
video.release()
cv2.destroyAllWindows()

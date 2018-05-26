import cv2
import numpy
from datetime import datetime
import pandas

# The first frame to be used as a base image
first_frame = None
# Keeps track of status changes
status_list = [None, None]
# Contains time periods of motion detections
times = []
# Pandas DataFrame
df = pandas.DataFrame(columns=["Start", "End"])

# Capture from camera
video = cv2.VideoCapture(-1)

while True:
    check, frame = video.read()
    # Status is 1 when an object is detected on screen
    status = 0
    # Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Get the first frame
    if first_frame is None:
        # First check if first frame is not black
        # (because my camera takes a second to open)
        if numpy.count_nonzero(frame) == 0:
            continue  # Skip this frame and get a "real" one
        first_frame = gray
        continue

    # Check difference between frames and base frame
    delta_frame = cv2.absdiff(first_frame, gray)
    # Threshold Frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # Make threshold smoother
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours
    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:  # 100x100 pixels
            continue
        status = 1  # Object detected
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    status_list.append(status)
    # Record time of status changes
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Show live images
    cv2.imshow("Capturing", frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    # Refresh every 1 msec
    key = cv2.waitKey(1)
    # Break loop
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

# Add times list to Pandas Dataframe
for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)
df.to_csv("Times.csv")

# Close camera
video.release()
cv2.destroyAllWindows()

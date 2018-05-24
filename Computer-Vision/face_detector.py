import cv2

# Load Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Load Image
img = cv2.imread("Path/to/image.jpg")
# Image to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the face
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)
# Draw the rectangles
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
# Show colored image
cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

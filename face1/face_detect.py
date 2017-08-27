# import the necessary packages
import cv2

# load our image and convert it to grayscale
image = cv2.imread("orientation_example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=10,
    minSize=(20, 20),
    flags=cv2.CASCADE_SCALE_IMAGE)
#flags=cv2.CV_HAAR_SCALE_IMAGE)   opencv 3 changed

# loop over the faces and draw a rectangle surrounding each
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
s="%d Faces" % len(rects)
# show the detected faces
cv2.imshow(s, image)
cv2.waitKey(0)


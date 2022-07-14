import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")

# Convert Blue Green Red image to a Gray image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Get you a Rectangle(frame)/ rectangle(s) of the face or faces, you may want to experiment on these numbers a bit
# The of the face is a numpy.ndarray. The print result of the faces is [[155 83 382 382]], which are coordinate of the rectangle of the faces
# If the Resolution of the image is not high, try to play with the scaleFactor to see if the result woould be any different
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors = 5)

# x,y are top left coorinate of the rectangle, w is the width, h is the height
# cv2.rectangle(img, starting_point, end_point, color tuple, thickness of rectangle)
for x, y, w, h in faces:
    img_w_rec = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img_w_rec,(int(img_w_rec.shape[1]/3),int(img_w_rec.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()

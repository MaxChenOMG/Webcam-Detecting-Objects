import cv2, time

# The parameter pass in is the Number of Webcam, access the video cam
video=cv2.VideoCapture(0)

# check is a boolean, frame represents the first image being captured in the video
check, frame = video.read()

# The program wait for three second before execute the next line
time.sleep(3)

# Converting the image to a Gray image
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cv2.imshow("Capturing", frame)
video.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

import cv2, time

# The parameter pass in is the Number of Webcam, access the video cam
video=cv2.VideoCapture(0)

while True:
    # check is a boolean, frame represents the first image being captured in the video
    check, frame = video.read()

    # print out the the array of image being captured
    print(check)
    print(frame)

    # Converting the image to a Gray image
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    # Press q on the keyboard to stop the program from running
    if key==ord('q'):
        break


video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

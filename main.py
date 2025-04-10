import cv2
import time

video = cv2.VideoCapture(0)

while True:
    time.sleep(1)
    check, frame = video.read()
    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()


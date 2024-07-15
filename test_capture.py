import cv2
import time

cap =  cv2.VideoCapture(0)


print('reading image after 3 sec')
time.sleep(2)

ret,frame = cap.read()
cv2.imshow('frame',frame)

if cv2.waitKey(0) and 0xff == ord('q'):
    cap.release()
    cv2.destroyAllWindows()
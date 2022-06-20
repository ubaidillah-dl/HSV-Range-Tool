import cv2
import numpy as np

def kamera(x):
    pass

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

cap=cv2.VideoCapture(0)
cv2.namedWindow('HSV Range Tool')
kernel=np.ones((5,5),np.uint8)

hl='Hue Low'
sl='Saturation Low'
vl='Value Low'
hh='Hue High'
sh='Saturation High'
vh='Value High'

cv2.createTrackbar(hl,'HSV Range Tool',0,180,kamera)
cv2.createTrackbar(sl,'HSV Range Tool',0,255,kamera)
cv2.createTrackbar(vl,'HSV Range Tool',0,255,kamera)
cv2.createTrackbar(hh,'HSV Range Tool',0,180,kamera)
cv2.createTrackbar(sh,'HSV Range Tool',0,255,kamera)
cv2.createTrackbar(vh,'HSV Range Tool',0,255,kamera)

while True:
    _,frame=cap.read()
    frame=rescale_frame(frame,percent=67.5)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hul=cv2.getTrackbarPos(hl,'HSV Range Tool')
    sal=cv2.getTrackbarPos(sl,'HSV Range Tool')
    val=cv2.getTrackbarPos(vl,'HSV Range Tool')
    huh=cv2.getTrackbarPos(hh,'HSV Range Tool')
    sah=cv2.getTrackbarPos(sh,'HSV Range Tool')
    vah=cv2.getTrackbarPos(vh,'HSV Range Tool')

    hsv_low=np.array([hul,sal,val])
    hsv_high=np.array([huh,sah,vah])

    mask=cv2.inRange(hsv,hsv_low,hsv_high)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    stacked=np.hstack((frame,res))
    cv2.imshow('HSV Range Tool',stacked)

    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()
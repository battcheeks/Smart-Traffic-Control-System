import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i=0

while(True):
    ret, frame = cap.read()
    a=frame.shape
    frame_gau=cv2.GaussianBlur(frame,(5,5),0)
    cv2.line(frame, (int(a[1]/2),0),(int(a[1]/2),int(a[0])) , (0,255,0), 2) 
    cv2.line(frame, (0,int(a[0]/2)),(int(a[1]),int(a[0]/2)) , (0,255,0), 2) 
    hsv=cv2.cvtColor(frame_gau,cv2.COLOR_BGR2HSV)
    lred=np.array([0,100,100],np.uint8)
    hred=np.array([10,255,255],np.uint8)
    red=cv2.inRange(hsv,lred,hred)
    kernel=np.ones((5,5),"uint8")
    red = cv2.dilate(red, kernel)
    res = cv2.bitwise_and(frame_gau, frame_gau, mask=red)
    contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    red_array=[]
    for pic,contour in enumerate(contours):
        area1=cv2.contourArea(contour)
        if(area1>3500):
            x,y,w,h=cv2.boundingRect(contour)
            if(w==h) & (x>320 & y<240):
                i=i+1
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
                M=cv2.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
                print(i,area1)
            a=str(x+(w/2))
            red_array.append(a)
    cv2.imshow('frame',frame)
    cv2.imshow("red mask",red)
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
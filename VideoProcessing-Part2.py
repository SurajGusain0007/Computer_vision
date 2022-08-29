# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:03:39 2022

@author: Suraj
"""

import cv2
##Here with the help of videoCapture fucntion we easily ready any video.

cap=cv2.VideoCapture("D:\dancevideo.mp4")

while True:
    ret,frame=cap.read()
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)
    #frame=cv2.resize(frame,(700,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("colorframe",frame)
    cv2.imshow("grayframe",gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Release everything if job is finished
cv2.release()
cv2.destroyAllWindows()       


##Capture  video from webcam and save it

# #Here parameter 0 is a path of any video use for webcam
# This will return video from the first webcam on your computer
import cv2
cap=cv2.VideoCapture(0)
print("check==",cap.isOpened())


#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('D:\output.avi', fourcc, 20.0, (640, 480))

#loop runs if capturing has been initialized

while(cap.isOpened()):
    # reads frames from a camera 
    # ret checks return at each frame
    ret,frame=cap.read()
    if ret==True:
     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("color_frame",frame)
     cv2.imshow("gray_frame",gray)
     out.write(frame)
     if cv2.waitKey(25) & 0xFF ==ord("q"):
        break
    else:
        print("Camera error")
cap.release()
out.release()
cv2.destroyAllWindows()
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:20:06 2022

@author: Suraj Gusain
"""
# #Here parameter 0 is a path of any video use for webcam
# This will return video from the first webcam on your computer
import cv2
camera="http://10.95.109.90:8080/video"
cap=cv2.VideoCapture(0)
cap.open(camera)
print("check==",cap.isOpened())


#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('D:\\vout.mp4', fourcc, 20.0, (640, 480))

#loop runs if capturing has been initialized

while(cap.isOpened()):
    # reads frames from a camera 
    # ret checks return at each frame
    ret,frame=cap.read()
    if ret==True:
     frame= cv2.resize(frame,(700,700))
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


#capture video from video
import cv2
import pafy
url="https://www.youtube.com/watch?v=t0Q2otsqC4I"
data=pafy.new(url)
vdata=data.getbest(preftype="mp4")
cap=cv2.VideoCapture(0)
cap.open(vdata.url)
print("check==",cap.isOpened())
#loop runs if capturing has been initialized
while(cap.isOpened()):
    # reads frames from a camera 
    # ret checks return at each frame
    ret,frame=cap.read()
    if ret==True:
     frame= cv2.resize(frame,(700,700))
     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("color_frame",frame)
     cv2.imshow("gray_frame",gray)
     if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    else:
        print("Camera error")
cap.release()
cv2.destroyAllWindows()
    
    
    

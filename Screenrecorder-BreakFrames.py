# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:52:31 2022

@author: Suraj Gusain
"""
#Screnrecorder 
import pyautogui as p
import cv2
import numpy as np

#create resolution
res=p.size()
print(res)
#filename in which we start recording
fn=input("please enter any file name and path")

#fix the frame rate

fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter(fn,fourcc,20.0,res)
#create recoring module

cv2.namedWindow("Live_Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording",(400,200))
while True:
    img=p.screenshot() #capture the image
    f=np.array(img)#convert image into array
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    out.write(f)
    cv2.imshow("Live_Recording",f)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
out.release()

#Break videos into multiple fraames
import cv2
cap=cv2.VideoCapture("D:\what.mp4")
ret,image=cap.read() #read the video

count=0
while True:
    if ret == True:
        cv2.imwrite("D:\frame\imgN%d.jpg"%count,image) #save frames as jpg file
        cap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = cap.read()
        cv2.imshow("res",image)
        print("read a new frame",count,ret)
        count=count+1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
          
cap.release()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:11:04 2022

@author: Suraj Gusain
"""
#image in color
import cv2
img1=cv2.imread("D:\suraj.jpeg",1) #accepts two paramters path and it specify the way in which image should be read.By default its value is 1
img1=cv2.resize(img1,(1200,700)) #width,#height
print(img1)
cv2.imshow("originalimage",img1) #acepts two parameters window name,imagename
cv2.waitKey()
cv2.destroyAllWindows()

#image in gray color

import cv2
img1=cv2.imread("D:\suraj.jpeg",0)
img1=cv2.resize(img1,(1200,700)) #width,#height
print(img1)
cv2.imshow("originalGrayimage",img1)
cv2.waitKey()
cv2.destroyAllWindows()

#flip the image

import cv2
img1=cv2.imread("D:\suraj.jpeg",0)
img1=cv2.resize(img1,(1200,700)) #width,#height
print(img1)
img1=cv2.flip(img1,0) #it accepts three paramters 1,0,-1
cv2.imshow("originalflipGrayimage",img1)
cv2.waitKey()
cv2.destroyAllWindows()

#image conversion project color image into gray color image
import cv2
#path=input("enter the path")
#print("You enter this ==",path)
img3=cv2.imread("D:\suraj.jpeg",0)
img3=cv2.resize(img3,(1200,700))
cv2.imshow("grayimage",img3)
k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite("D:soooraj.png",img3)
else:
    cv2.destroyAllwindows()

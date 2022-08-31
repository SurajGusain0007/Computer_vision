# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:51:57 2022

@author: Suraj Gusain
"""

import numpy as np
import cv2



# mouse callback function
def draw(event,x,y,flags,param):
    print("x",x)
    print("x",y)
    print("flags",flags)
    print("param",param)
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        cv2.circle(img,(x,y),100,(125,0,255),5)
        cv2.imshow("image",img)
        
def draw_circle(event,x,y,flags,param):
    print("x",x)
    print("x",y)
    print("flags",flags)
    print("param",param)

   
    if event == cv2.EVENT_RBUTTONDBLCLK:
   
       cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
       cv2.imshow("image_suraj",img)
 
        
        
cv2.namedWindow(winname = "image")  

cv2.namedWindow(winname = "image_suraj")    
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
#cv2.imshow("image",img)
#cv2.imshow("image_suraj",img)
cv2.setMouseCallback("image",draw)
cv2.setMouseCallback("image_suraj",draw_circle)

cv2.waitKey(0)
cv2.destroyAllWindows()

#You don't call draw_circle, openCV will call it for you on a mouse event with the proper event 
#and coordinates, you just specify which function to be called for what window in 
#setMouseCallback

#if you need additional variables you can send them via param

#You can have multiple windows with a different mouse action set for each one cv2.namedwindow




#create a function which help to find coordinate

import cv2
import numpy as np
def mouse_event(event, x, y, flg, param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flg==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN 
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
           
        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125 ,100), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)
img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('H:\\Data\\thor.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

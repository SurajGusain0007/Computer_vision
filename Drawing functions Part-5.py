# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:33:17 2022

@author: Suraj Gusain
"""
#Drawing function in cv
import cv2
import numpy as np
img=cv2.imread("D:\\thor.jpg")
cv2.resize(img,(500,600))
cv2.imshow("aven",img)

#Here line accept 5 parameter(img,starting,ending,color,thickbess)
img=cv2.line(img,(0,0),(200,200),(245,7,31),8)
#img=np.zeros([512,512,3],np.uint8)*255 #for black screen uint-unsigned int

img=np.ones([512,512,3],np.uint8)*255 #for white screen


##Here arrow line accept 5 parameter(img,starting,ending,color,thickness)
img=cv2.arrowedLine(img,(0,125),(255,255),(245,7,31),8)

##Rectangle:-Here arrow line accept 5 parameter(img,starting,ending,color,thickness)
img=cv2.rectangle(img,(400,20),(500,123),(245,7,31),8)

#
##Rectangle:-Here arrow line accept 5 parameter(img,starting,ending,color,thickness)
img=cv2.rectangle(img,(600,20),(800,123),(245,7,31),-1)


##Circus:-Here arrow line accept 5 parameter(img,starting,radius,color,thickness)
img=cv2.circle(img,(440,120),63,(245,7,31),-5)

font=cv2.FONT_HERSHEY_COMPLEX
#puttext-accept(img,text,start,font,fontsize,color,thickness,linetype)
img=cv2.putText(img,'THOR',(20,500),font,4,(0,125,255),10,cv2.LINE_AA)

#ellipse-accept(img,start_cor,(lenghts,height),color,thickness)
img=cv2.ellipse(img,(300,600),(100,50),0,0,180,155,5)


cv2.imshow("aven",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

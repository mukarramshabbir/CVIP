import cv2
import numpy as np

image=cv2.imread("win.png")

B=image[:,:,0]
G=image[:,:,1]
R=image[:,:,2]
print(image.shape)
#cv2.imshow("Test Image", image)

#cv2.imshow("Blue:",B)
#cv2.imshow("Green:",G)
#cv2.imshow("Red:",R)
#cv2.waitKey(0)


Z=np.zeros((image.shape[0],image.shape[1]))
image[:,:,0]=Z
image[:,:,1]=Z

cv2.imshow("Blue Image:",image)
cv2.waitKey(0)

ROI=image[0:200,0:500,:]
image[200:400,1000:1500,:]=ROI

cv2.imshow("New Image:",image)
cv2.waitKey(0)
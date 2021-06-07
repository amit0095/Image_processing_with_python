#import Library
import cv2
import numpy as np

#Read Images[all images dimensions are same.]
dodge_challenger=cv2.imread('Dodge Challenger.jpg')
Dr_Strange=cv2.imread('Dr_ Strange.jpg')
dr_strange=cv2.imread('dr strange.jpg')
Doutor_Estranho=cv2.imread("Doutor Estranho.jpg")

#making collages
image1=np.hstack((dodge_challenger,Dr_Strange))
image2=np.hstack((dr_strange,Doutor_Estranho))

#adding collage 1 and 2 both
final_image=np.concatenate((image1,image2), axis=0)

#showing final collage
cv2.imshow("final_image",final_image)
cv2.waitKey()
cv2.destroyAllWindows()

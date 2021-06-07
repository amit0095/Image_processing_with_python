#import Library
import cv2
import numpy as np

#creating black colored new image
colorpic=np.zeros((500,500,3))
colorpic[:,:]=[0,0,0]

#white strips in between
colorpic[:,230:265]=[255,255,255]
colorpic[230:265,:]=[255,255,255]

#Red colored box
colorpic[35:195,35:195]=[0,0,255]
#Sky colored box
colorpic[300:465,35:195]=[0,255,242]
#Yellow colored box
colorpic[35:195,300:465]=[255, 30, 0]
#Green colored box
colorpic[300:465,300:465]=[0,255,0]

#Image Showing
cv2.imshow("Colored_square_box",colorpic)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2
import numpy as np
colorpic=np.zeros((500,500,3))
colorpic[:,:]=[0,0,0]
colorpic[:,230:265]=[255,255,255]
colorpic[230:265,:]=[255,255,255]
colorpic[35:195,35:195]=[0,0,255]
colorpic[300:465,35:195]=[0,255,242]
colorpic[35:195,300:465]=[255, 30, 0]
colorpic[300:465,300:465]=[0,255,0]
cv2.imshow("Colored_square_box",colorpic)
cv2.waitKey()
cv2.destroyAllWindows()

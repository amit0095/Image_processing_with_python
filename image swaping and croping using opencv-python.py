#import library
import cv2

# read image files
photo1=cv2.imread('photo1.jpg')
photo2=cv2.imread('photo2.jpg')

# showing image of photo1
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()

#Croping image of photo1
ph1=photo1[180:421,300:687]

# showing image of ph1
cv2.imshow('hi',ph1)
cv2.waitKey()
cv2.destroyAllWindows()

# showing image of photo2
cv2.imshow('hi',photo2)
cv2.waitKey()
cv2.destroyAllWindows()

#Croping image of photo2
ph2=photo2[180:421,300:687]

# showing image of ph2
cv2.imshow('hi',ph2)
cv2.waitKey()
cv2.destroyAllWindows()

# restoring photo1 which's croped pixel is removed now from center
photo1=cv2.imread('photo1.jpg')

# restoring photo2 which's croped pixel is removed now from center
photo2=cv2.imread('photo2.jpg')

#swap croping image of ph2 to photo1
photo1[180:421,300:687]=ph2

#swap croping image of ph2 to photo2
photo2[180:421,300:687]=ph1

#showing new swaped photo1
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()

#showing new swaped photo2
cv2.imshow('hi',photo2)
cv2.waitKey()
cv2.destroyAllWindows()

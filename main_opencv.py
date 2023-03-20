import cv2

img = cv2.imread('test.jpg')

#print(img)

img = cv2.resize(img, (400, 1000))

cv2.imshow('result', img)

cv2.waitKey(0)
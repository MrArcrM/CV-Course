import cv2
import numpy as np


img = cv2.imread('lenna.jpeg')
# cv2.imshow('lenna', img)
#
# key = cv2.waitKey()
# if key == 27:  # if 'esc' is pressed
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)

# Gaussian Kernel Effect
# g_img = cv2.GaussianBlur(img, (7, 7), 1)
# cv2.imshow('gaussian_blur_lenna', g_img)
# key = cv2.waitKey()
# if key == 27:  # if 'esc' is pressed
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)

img = cv2.imread('lenna.jpg')
# create sift class
sift = cv2.xfeatures2d.SIFT_create()
# detect SIFT
kp = sift.detect(img,None)   # None for mask
# compute SIFT descriptor
kp, des = sift.compute(img, kp)
print(des.shape)
img_sift= cv2.drawKeypoints(img,kp,outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('lenna_sift.jpg', img_sift)
key = cv2.waitKey()
if key == 27:  # if 'esc' is pressed
    cv2.destroyAllWindows()
    cv2.waitKey(1)
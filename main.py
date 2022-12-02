#import RPi.GPIO as GPIO
from funcStitch import stitching
import cv2

#allImages = [["./testImages/whiteboard-test3/20221118_124555.jpg", "./testImages/whiteboard-test3/20221118_124558.jpg", "./testImages/whiteboard-test3/20221118_124601.jpg"]]
#temp = "./outputImages/firstTemp.jpg"
outputPath = "./outputImages/whiteboardOutput.jpg"

allImages = [["./testImages/window-test/left.jpg", "./testImages/window-test/mid.jpg", "./testImages/window-test/right.jpg"]]

img1 = cv2.imread(allImages[0][0])
img2 = cv2.imread(allImages[0][1])
img3 = cv2.imread(allImages[0][2])

temp = stitching(img1, img2)
firstOutput = stitching(temp, img3)

cv2.imwrite(outputPath, firstOutput)
cv2.imshow("Result", firstOutput)

cv2.waitKey(0)

# for i in range(1, 10):

#     img1 = allImages[i][0]
#     img2 = allImages[i][1]
#     img3 = allImages[i][2]
#     temp = "./outputImages/temp.jpg"

#     stitching(img1, img2, temp)
#     stitching(temp, img3, temp)
#     stitching(outputPath, temp)
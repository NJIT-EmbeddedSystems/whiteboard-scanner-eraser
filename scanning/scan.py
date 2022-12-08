from stitch import stitching
from removeBorder import removeBorder
import cv2

#Storing image paths and output paths
allImages = [["./testImages/whiteboard-test2/20221118_121053.jpg", "./testImages/whiteboard-test2/20221118_121056.jpg", "./testImages/whiteboard-test2/20221118_121058.jpg"]]
tempPath = "./outputImages/firstTemp.jpg"
temp2Path = "./outputImages/secondTemp.jpg"
outputPath = "./outputImages/whiteboardOutput.jpg"

#Reading in images with OpenCV
img1 = cv2.imread(allImages[0][0])
img2 = cv2.imread(allImages[0][1])
img3 = cv2.imread(allImages[0][2])

#TEMP 1
temp = stitching(img1, img2)

cv2.imwrite(tempPath, temp)
temp = removeBorder(tempPath)


#TEMP 2
temp2 = stitching(img2, img3)

cv2.imwrite(temp2Path, temp2)
temp2 = removeBorder(temp2Path)


#FINAL
firstOutput = stitching(temp, temp2)

cv2.imwrite(outputPath, firstOutput)
firstOutput = removeBorder(outputPath)

cv2.imwrite(outputPath, firstOutput)

#Used for repeating over length of whiteboard
# for i in range(1, 10):

#     img1 = allImages[i][0]
#     img2 = allImages[i][1]
#     img3 = allImages[i][2]
#     temp = "./outputImages/temp.jpg"

#     stitching(img1, img2, temp)
#     stitching(temp, img3, temp)
#     stitching(outputPath, temp)
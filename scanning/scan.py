from stitch import stitching
import cv2

#Getting raw photos (in jpg)



#Read images into CV2 image objects



#Stitch the images




#Save the images






#Storing image paths and output paths
allImages = [["./testImages/whiteboard-test2/20221118_121053.jpg", "./testImages/whiteboard-test2/20221118_121056.jpg", "./testImages/whiteboard-test2/20221118_121058.jpg"]]
# tempPath = "./outputImages/firstTemp.jpg"
# temp2Path = "./outputImages/secondTemp.jpg"
outputPath = "./outputImages/whiteboardOutput.jpg"

#Reading in images with OpenCV
# img1 = cv2.imread(allImages[0][0])
# img2 = cv2.imread(allImages[0][1])
# img3 = cv2.imread(allImages[0][2])

imgList = list(map(cv2.imread, allImages[0]))

#TEMP 1
# temp = stitching(imgList[0], imgList[1])

#temp = removeBorder(tempPath)
# cv2.imwrite(tempPath, temp)


#TEMP 2
# temp2 = stitching(imgList[1], imgList[2])

#temp2 = removeBorder(temp2Path)
# cv2.imwrite(temp2Path, temp2)


#FINAL
firstOutput = stitching(imgList[0], imgList[1], imgList[2])

#firstOutput = removeBorder(firstOutput)
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
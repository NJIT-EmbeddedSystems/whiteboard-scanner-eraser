from stitch import stitching
import cv2
import glob

# Getting raw photos (in jpg)
path = "./testImages/whiteboard-test2/"
allImages = glob.glob(path + "*")

outputPath = "./outputImages/whiteboardOutput.jpg"

# allImages = [["./testImages/whiteboard-test2/20221118_121053.jpg", "./testImages/whiteboard-test2/20221118_121056.jpg", "./testImages/whiteboard-test2/20221118_121058.jpg"]]
# tempPath = "./outputImages/firstTemp.jpg"
# temp2Path = "./outputImages/secondTemp.jpg"




# Read images into CV2 image objects
imgList = list(map(cv2.imread, allImages))

# img1 = cv2.imread(allImages[0][0])
# img2 = cv2.imread(allImages[0][1])
# img3 = cv2.imread(allImages[0][2])





# Stitch the images vertically
#TEMP 1
# temp = stitching(imgList[0], imgList[1])

#temp = removeBorder(tempPath)
# cv2.imwrite(tempPath, temp)

#TEMP 2
# temp2 = stitching(imgList[1], imgList[2])

#temp2 = removeBorder(temp2Path)
# cv2.imwrite(temp2Path, temp2)

#FINAL
output = stitching(imgList[0], imgList[1], imgList[2])

#firstOutput = removeBorder(firstOutput)
cv2.imwrite(outputPath, output)



# Stitch the images horizontally





#Used for repeating over length of whiteboard
# for i in range(1, 10):

#     img1 = allImages[i][0]
#     img2 = allImages[i][1]
#     img3 = allImages[i][2]
#     temp = "./outputImages/temp.jpg"

#     stitching(img1, img2, temp)
#     stitching(temp, img3, temp)
#     stitching(outputPath, temp)
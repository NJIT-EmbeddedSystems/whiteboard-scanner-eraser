from stitch import stitching
import cv2
import glob

# Getting raw photos (in jpg)
path = "./testImages/whiteboard-test2/"
allImages = glob.glob(path + "*")

outputPath = "./outputImages/whiteboardOutput.jpg"


# Read images into CV2 image objects
imgList = list(map(cv2.imread, allImages))


# Stitch the images vertically

output = stitching(imgList[0], imgList[1], imgList[2])
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
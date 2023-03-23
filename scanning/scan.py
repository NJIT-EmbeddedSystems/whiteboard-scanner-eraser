## top-level scan file. main driving pipeline here.
## 

from stitch import stitching2
from removeBorder import removeBorder
import cv2
import imutils
import glob
import numpy as np

# Getting raw photos (in jpg)
# placeholder for internal testing
path = "./testImages/whiteboard-test2/" #FIXME : add real path of raw images
allImages = glob.glob(path + "*")
imagePaths = []

outputPath = "./outputImages/testOutput.jpg"


# Read images into CV2 image objects
imgList = list(map(cv2.imread, allImages))


# Remove Fisheye Distortion



# Stitch the images vertically
output = stitching2(imgList[0], imgList[1]) # FIXME : stitch two images vertically


result = cv2.addWeighted(output, 0.9, output, 1.1, 0) # play with weight numbers, affected by lighting?
cv2.imwrite(outputPath, result)

# might not need to do this
## #Rotate vertically stitched image 
## rotated = cv2.rotate(result, cv2.ROTATE_90_CLOCKWISE)
## cv2.imwrite(outputPath, rotated)


# Stitch the images horizontally
## take each output vertical stitch in array
## take first, append next image
## keep appending until reach end of board

#Used for repeating over length of whiteboard
# for i in range(1, 10):

#     img1 = allImages[i][0]
#     img2 = allImages[i][1]
#     img3 = allImages[i][2]
#     temp = "./outputImages/temp.jpg"

#     stitching(img1, img2, temp)
#     stitching(temp, img3, temp)
#     stitching(outputPath, temp)
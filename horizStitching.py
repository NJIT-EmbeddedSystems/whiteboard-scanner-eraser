import cv2
import numpy as np
import argparse
import imutils
from imutils import paths

# reads file paths from the command line
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", type=str, required=True,
# 	help="path to input directory of images to stitch")
# ap.add_argument("-o", "--output", type=str, required=True,
# 	help="path to the output image")
# args = vars(ap.parse_args())

inputPath = "./testImages"
outputPath = "./testImages/output.jpg"

# gets all image paths from folder
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(inputPath)))
images = []

# loop over the image paths, load each one, and add them to our images to stitch list
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)

# initialize OpenCV's image stitcher object and then perform the image stitching
print("[INFO] stitching images...")
stitcher = cv2.Stitcher_create() 
(status, stitched) = stitcher.stitch(images)

# if the status is '0', then OpenCV successfully performed image stitching
if status == 0:
	# write the output stitched image to disk
	cv2.imwrite(outputPath, stitched)

	# display the output stitched image to our screen
	#cv2.imshow("Stitched", stitched)
	#cv2.waitKey(0)

# otherwise the stitching failed, likely due to not enough keypoints) being detected
else:
	print("[INFO] image stitching failed ({})".format(status))
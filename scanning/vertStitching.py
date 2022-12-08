import cv2
import numpy as np
import imutils
from panorama import Stitcher

def vertStitching(img1, img2, img3):

    # imageA = cv2.imread("./testImages/window-test/left.jpg")
    # imageB = cv2.imread("./testImages/window-test/mid.jpg")
    imageA = cv2.imread("./testImages/whiteboard-test3/20221118_124555.jpg")
    imageB = cv2.imread("./testImages/whiteboard-test3/20221118_124558.jpg")
    imageA = imutils.resize(imageA, width=400)
    imageB = imutils.resize(imageB, width=400)

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

    # cv2.imshow("Image A", imageA)
    # cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    cv2.imshow("Result", result)
    cv2.waitKey(0)

    #add third image

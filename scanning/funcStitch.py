import cv2
import imutils
from panorama import Stitcher

def stitching(img1, img2):

    # imageA = cv2.imread(img1)
    # imageB = cv2.imread(img2)
    imageA = img1
    imageB = img2
    #imageA = imutils.resize(imageA, width=400)
    #imageB = imutils.resize(imageB, width=400)

    #cv2.imshow("Image A", imageA)
    #cv2.imshow("Image B", imageB)

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

    # cv2.imshow("Image A", imageA)
    # cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    cv2.waitKey(0)

    #cv2.imwrite(output, result)
    return result
from panorama import Stitcher
from removeBorder import removeBorder

def stitching(img1, img2, img3):

    #imageA = imutils.resize(imageA, width=400)
    #imageB = imutils.resize(imageB, width=400)

    #cv2.imshow("Image A", imageA)
    #cv2.imshow("Image B", imageB)

    stitcher = Stitcher()
    
    (result, vis) = stitcher.stitch([img1, img2], showMatches=True)
    result = removeBorder(result)

    (result, vis) = stitcher.stitch([result, img3], showMatches=True)
    result = removeBorder(result)

    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)

    return result
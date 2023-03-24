## Contains the function to stitch either two or three images together.
##

from panorama import Stitcher
from removeBorder import removeBorder

def stitching3(img1, img2, img3):

    stitcher = Stitcher()
    
    # (result, vis) = stitcher.stitch([img1, img2], showMatches=True)
    result = stitcher.stitch([img1, img2])
    result = removeBorder(result)

    # (result, vis) = stitcher.stitch([result, img3], showMatches=True)
    result2 = stitcher.stitch([result, img3])
    result2 = removeBorder(result2)

    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)

    return result2


def stitching2(img1, img2):

    stitcher = Stitcher()
    
    # (result, vis) = stitcher.stitch([img1, img2], showMatches=True)
    result = stitcher.stitch([img1, img2])
    result = removeBorder(result)

    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)

    return result
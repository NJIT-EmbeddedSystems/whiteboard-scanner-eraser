from stitch import stitching
import cv2
import glob

# Getting raw photos (in jpg)
path = "./testImages/whiteboard-test2/"
allImages = glob.glob(path + "*")

outputPath = "./outputImages/testOutput.jpg"


# Read images into CV2 image objects
imgList = list(map(cv2.imread, allImages))


# Stitch the images vertically

output = stitching(imgList[0], imgList[1], imgList[2])
cv2.imwrite(outputPath, output)


result = cv2.addWeighted(output, 0, output, 1.1, 1.1)
cv2.imwrite(outputPath, result)


# def brightness( im_file ):
#    im = Image.open(im_file).convert('L')
#    stat = ImageStat.Stat(im)
#    return stat.mean[0]

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
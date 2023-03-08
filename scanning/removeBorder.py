import numpy as np
import cv2
import copy

def removeBorder(original):
    # keep a copy of original image
    # original = cv2.imread(imgPath)

    # Read the image, convert it into grayscale, and make in binary image for threshold value of 1.
    # img = cv2.imread(imgPath, 0)
    img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # use binary threshold, all pixel that are beyond 3 are made white
    _, thresh_original = cv2.threshold(img, 3, 255, cv2.THRESH_BINARY)

    # Now find contours in it.
    thresh = copy.copy(thresh_original)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # get contours with highest height
    lst_contours = []
    for cnt in contours:
        ctr = cv2.boundingRect(cnt)
        lst_contours.append(ctr)
    x,y,w,h = sorted(lst_contours, key=lambda coef: coef[3])[-1]

    # draw contours
    ctr = copy.copy(original)
    cv2.rectangle(ctr, (x,y),(x+w,y+h),(0,255,0),2)

    crop = original[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop)
    # cv2.waitKey(0)

    return crop
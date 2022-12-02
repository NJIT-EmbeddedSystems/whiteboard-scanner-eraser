#import RPi.GPIO as GPIO
import horizStitching
import vertStitching


for i in range(10):

    if i == 0:
        vertStitching(img1, img2, img3, output)
        continue

    vertStitching(img1, img2, img3, finalOutput)
    horizStitching(finalOutput, output1, output2)
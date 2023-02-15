#importing Button, Servo, and Motor library to control buttons, servo and dc motors, respectively
from gpiozero import Button,Servo,Motor
import time
import piCamera

class EraserServos:
    def __init__(self, *args: Servo):
        self.servos=[]
        for s in args:
            if s != None:
                self.servos.append(s)
    def min(self):
        for s in self.servos:
            s.min()
    def max(self):
        for s in self.servos:
            s.max()
    def printValue(self):
        for s in self.servos:
            print("servo #",self.servos.index(s),":",s.value)
    def modifyValue(self, val):
        for s in self.servos:
            s.value = val


#initializing input buttons and limit switches (also classified as buttons)
scanButton = #Button(pin#)
eraseButton = #Button(pin#)
dualButton = #Button(pin#)

#Have to see if the limit swithces are normally open or normally closed
limitLeft = #Button(pin#)
limitRight = #Button(pin#)

#initializing output devices
eraserServos = #EraserServos(#Servo(pin #, initial_value = 0), #Servo(pin #,initial_value = 0), #Servo(pin #,initial_value = 0))
eraserMotor_DC = #Motor(forward= forward pin#, backward = backward pin#)

#initializing Camera
camera = PiCamera()

# takes into consideration possiblity of installation on both left and right sides
intialLimit = limitLeft
finalLimit = limitRight
# uses an attribute for position: left or right
position = "left" # left by default for now until the attribute is defined

if position == "right":
    intialLimit = limitRight
    finalLimit = limitLeft
 
# Defining erase functions
def erase(): 
  #Places felt on board and begin moving across board
    eraserServos.max()
    time.sleep(1)
    eraserMotor_DC.forward()
    while(finalLimit == 0):
        continue
    #should work for both normally closed and normally open limit switches
    #make motor return to starting position once it reaches the end of the board
    eraserMotor_DC.reverse()
    #pick felt back up when the eraser reaches its starting position
    while(intialLimit == 0):
        continue
    eraserMotor_DC.stop()
    time.sleep(1)
    eraserServos.modifyValue(0)
    return

def scan():
    timeBetweenPics = 1 #adjustable picture taking delay based on time
    runtime = time.time()
    camera.capture() #take initial image
    while finalLimit == 0: #or 1 if it's a normally closed limit switch
        eraserMotor_DC.forward()
        if runtime == timeBetweenPics:
            eraserMotor_DC.stop()
            time.sleep(1)
            camera.capture()
            time.sleep(1)
            runtime = time.time() #restart timer
    #when finalLimit is reached, return to starting position
    eraserMotor_DC.reverse()
    while(intialLimit == 0): #or 1 if it's a normally closed limit switch
        continue
    eraserMotor_DC.stop()
    time.sleep(1)
    return
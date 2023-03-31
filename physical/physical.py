#importing Button, Servo, and Motor library to control buttons, servo and dc motors, respectively
from threading import active_count
from gpiozero import Button,Servo,Motor,OutputDevice
import time
from picamera import PiCamera # FIXME : need to use picamera 2
import datetime

# constants
SCANBUTTON   = 17
ERASEBUTTON  = 27
DUALBUTTON   = 22
LIMITLEFT    = 5
LIMITRIGHT   = 6
ERASERSERVOS = [13,19,26]
ERASERMOTORS = [23,24]

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
scanButton = Button(SCANBUTTON)
eraseButton = Button(ERASEBUTTON)
dualButton = Button(DUALBUTTON)

#Have to see if the limit swithces are normally open or normally closed
limitLeft = Button(LIMITLEFT)
limitRight = Button(LIMITRIGHT)

#initializing output devices
## FIXME : need to drive all servos from one pin
eraserServos = EraserServos(Servo(ERASERSERVOS[0], initial_value = 0), Servo(ERASERSERVOS[1],initial_value = 0), Servo(ERASERSERVOS[2],initial_value = 0))

motorRelay1 = OutputDevice(ERASERMOTORS[0], active_high = False, initial_value = False)
motorRelay2 = OutputDevice(ERASERMOTORS[1], active_high = False, initial_value = False)

def relayForward():
    motorRelay1.on()
    motorRelay2.off()

def relayBackward():
    motorRelay1.off()
    motorRelay2.on()

def relayStop():
    motorRelay1.off()
    motorRelay2.off()


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
    relayForward()
    while(finalLimit == 0):
        continue
    #should work for both normally closed and normally open limit switches
    #make motor return to starting position once it reaches the end of the board
    relayStop()
    time.sleep(1)
    relayBackward()
    #pick felt back up when the eraser reaches its starting position
    while(intialLimit == 0):
        continue
    relaystop()
    time.sleep(1)
    eraserServos.modifyValue(0)
    return

def scan():
    timeBetweenPics = 1 #adjustable picture taking delay based on time
    runtime = time.time()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    camera.capture('img{}.jpg'.format(current_time)) #take initial image
    while finalLimit == 0: #or 1 if it's a normally closed limit switch
        relayForward()
        if runtime == timeBetweenPics:
            relayStop()
            time.sleep(1)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            camera.capture('img{}.jpg'.format(current_time)) 
            time.sleep(1)
            runtime = time.time() #restart timer
    #when finalLimit is reached, return to starting position
    relayStop()
    time.sleep(1)
    relayBackward()
    while(intialLimit == 0): #or 1 if it's a normally closed limit switch
        continue
    relayStop()
    time.sleep(1)
    return

if scanButton.is_pressed():
    scan()
elif eraseButton.is_pressed():
    erase()

#importing Button, Servo, and Motor library to control buttons, servo and dc motors, respectively
from gpiozero import Button,Servo,Motor,OutputDevice
import time

# constants
ERASEBUTTON  = 27
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

eraseButton = Button(ERASEBUTTON)

#Have to see if the limit swithces are normally open or normally closed
limitLeft = Button(LIMITLEFT)
limitRight = Button(LIMITRIGHT)

#initializing output devices
## FIXME : need to drive all servos from one pin

motorRelay1 = OutputDevice(ERASERMOTORS[0], active_high = False, initial_value = False)
motorRelay2 = OutputDevice(ERASERMOTORS[1], active_high = True, initial_value = True)
   
def relayForward():
    print("before relay1: ", motorRelay1.value)
    print("before relay2: ", motorRelay2.value)
    motorRelay1.toggle()
    motorRelay2.toggle()
    print("relay1: ", motorRelay1.value)
    print("relay2: ", motorRelay2.value)

def relayBackward():
    print("before relay1: ", motorRelay1.value)
    print("before relay2: ", motorRelay2.value)
    motorRelay1.toggle()
    motorRelay2.toggle()
    print("relay1: ", motorRelay1.value)
    print("relay2: ", motorRelay2.value)

def relayStop():
    print("before relay1: ", motorRelay1.value)
    print("before relay2: ", motorRelay2.value)
    motorRelay1.off()
    motorRelay2.on()
    print("relay1: ", motorRelay1.value)
    print("relay2: ", motorRelay2.value)

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
#    eraserServos.max()
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
    relayStop()
    time.sleep(1)
#    eraserServos.modifyValue(0)
    return

erase()
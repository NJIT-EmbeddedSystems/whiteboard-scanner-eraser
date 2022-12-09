#importing Button, Servo, and Motor library to control buttons, servo and dc motors, respectively
# importing Device and Mock Factory to assign mock pins for testing
from gpiozero import Button,Servo,Motor, Device
from gpiozero.pins.mock import MockFactory, MockPWMPin
import time, threading, os

Device.pin_factory = MockFactory(pin_class=MockPWMPin)

os.system("cls") 

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
            print("\33[0mservo #",self.servos.index(s),":",s.value)
    def modifyValue(self, val):
        for s in self.servos:
            s.value = val

#initializing input buttons and limit switches (also classified as buttons)
scanButton = Button(16)
eraseButton = Button(20)
dualButton = Button(21)

#Have to see if the limit swithces are normally open or normally closed
limitLeft = Button(23)
limitRight = Button(24)

#initializing output devices
eraserServos = EraserServos(Servo(17,initial_value=0),Servo(27,initial_value=0),Servo(22,initial_value=0))

eraserMotor_DC = Motor(forward= 5, backward = 6)
cameraMotor_DC = Motor(forward= 19, backward = 26)

intialLimit = limitLeft
finalLimit = limitRight
# uses an attribute for position: left or right
position = "left" # left by default for now until the attribute is defined

if position == "right":
    intialLimit = limitRight
    finalLimit = limitLeft
 
# Modded Erase function for simulation
def eraseSimulation(): 
   time.sleep(1)
  #Places felt on board and begin moving across board
   eraserServos.max()
   print("\33[31mServos Down\n")
   time.sleep(1)
   eraserMotor_DC.forward()
   print("\33[31mMotor started moving forward\n")
   time.sleep(10)
   finalLimit.pin.drive_low() # simulating the pressing of the limit
   print("\33[31mRight Limit pressed\n")
   if finalLimit.is_pressed:
      time.sleep(1)
      finalLimit.pin.drive_high() # simulating the release of the limit
      print("\33[31mRight Limit released\n")
      eraserMotor_DC.reverse()
      print("\33[31mMotor in Reverse\n")
      time.sleep(10)
      intialLimit.pin.drive_low() # simulating the pressing of the limit
      print("\33[31mLeft Limit pressed\n")
      #pick felt back up when the eraser reaches its starting position
      if intialLimit.is_pressed:
        time.sleep(1)
        intialLimit.pin.drive_high() # simulating the release of the limit
        print("\33[31mRight Limit released\n")
        eraserServos.modifyValue(0)
        print("\33[31mServos Up\n")
        eraserMotor_DC.stop()
        print("\33[31mMotor Stopped\n")
        time.sleep(2)
        return

# Simulation function that reports the status of each part every second
def sim():
        t = threading.Timer(1, sim).start()
        print("\33[0mLimit Switch 1 State:", intialLimit.value)
        print("\33[0mLimit Switch 2 State: ", finalLimit.value)
        eraserServos.printValue()
        print("\33[0mMotor Active?:",eraserMotor_DC.is_active)
        print("\33[0mMotor Speed:", eraserMotor_DC.value)
        print()

eraserThread = threading.Thread(target = eraseSimulation, args = ())
simulationThread = threading.Thread(target = sim, args = (), daemon=True)

simulationThread.start()
eraserThread.start()

eraserThread.join()
simulationThread.join()
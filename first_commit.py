#importing Button, Servo, and Motor library to control buttons, servo and dc motors, respectively
from gpiozero import Button,Servo,Motor

#initializing input buttons and limit switches (also classified as buttons)
scanButton = #Button(pin#)
eraseButton = #Button(pin#)
dualButton = #Button(pin#)

#Have to see if the limit swithces are normally open or normally closed
limitLeft = #Button(pin#)
limitRight = #Button(pin#)

#initializing output devices
eraserServo = #Servo(pin #)
eraserMotor_DC = #Motor(forward= forward pin#, backward = backward pin#)
cameraMotor_DC = #Motor(forward= forward pin#, backward = backward pin#)


 
#servo.min() and servo.max() can be switched depending on orientation of the servo in prototype
def erase(): 
  #Places felt on board and begin moving across board
   eraserServo.max()
   eraserMotor_DC.forward()
   #should work for both normally closed and normally open limit switches
   #make motor return to starting position once it reaches the end of the board
   if limitRight.is_pressed():
      eraserMotor_DC.backward()
      #pick felt back up when the eraser reaches its starting position
      if limitLeft.is_pressed():
        eraserServo.min()
        return

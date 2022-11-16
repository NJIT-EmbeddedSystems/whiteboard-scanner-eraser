Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #importing Servo and Motor library to control servo and dc motor, respectively
... from gpiozero import Button,Servo,Motor
... 
... #initializing input buttons and limit switches (also classified as buttons)
... scanButton = #Button(pin#)
... eraseButton = #Button(pin#)
... dualButton = #Button(pin#)
... limitLeft = #Button(pin#)
... limitRight = #Button(pin#)
... 
... #initializing output devices
... eraserServo = #Servo(pin #)
... eraserMotor_DC = #Motor(forward= forward pin#, backward = backward pin#)
... cameraMotor_DC = #Motor(forward= forward pin#, backward = backward pin#)
... 
... 
... 
... #servo.min() and servo.max() can be switched depending on orientation of the servo in prototype
... 
... def erase(): 
...     #Places felt on board and begin moving across board
...     eraserServo.max()
...     eraserMotor_DC.forward()
...     #should work for both normally closed and normally open limit switches
...     #make motor return to starting position once it reaches the end of the board
...     if limitRight.is_pressed():
...         eraserMotor_DC.backward()
...         #pick felt back up when the eraser reaches its starting position
...         if limitLeft.is_pressed():
...             eraserServo.min()
...             return
... 
... def scan():
...     #needs some function to turn on cameras, will have to collaborate with camera subgroup
...     #makes cameras pan across board and return after hitting the limit switch
...     cameraMotor_DC.forward()
...     if limitLeft.is_pressed():
...       #needs a function to turn off cameras, maybe importing RPi.GPIO to supply power through specific pins will work?
...         cameraMotor_DC.backward()
...         if limitLeft.is_pressed():
...             return
...        
... #button interface
... #constantly scans for a button being pressed and calls a corresponding function
... while True:
...   if eraseButton.is_pressed():
...     erase()
...   else if scanButton.is_pressed():
...     scan()
...   else if dualButton.is_pressed():
...     scan()
...     erase()

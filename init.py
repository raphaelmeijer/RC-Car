#!/usr/bin/python
# Import required libraries
import sys
import time
from Sensors import Sensors
from Sequence import Sequence
from Wheel import Wheel
import RPi.GPIO as GPIO
 
Sequence    = Sequence()

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPinsR   = [2,3,4,17]
StepPinsL   = [27,22,10,9]
Speed       = Sequence.FORWARD

# Set all pins as output
for pin in StepPinsL:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Set all pins as output
for pin in StepPinsR:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
Sensors	= Sensors( GPIO ) 
leftWheel   = Wheel( StepPinsL, 1, -1 )
rightWheel  = Wheel( StepPinsR, 1, 1 )

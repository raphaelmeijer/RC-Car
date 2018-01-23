#!/usr/bin/python
# Import required libraries
import sys
import time
from Sensors import Sensors
from Sequence import Sequence
import RPi.GPIO as GPIO
 
# Init classes
Sensors     = Sensors()
Sequence    = Sequence()

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPinsR   = [2,3,4,17]
StepPinsL   = [27,22,10,9]
SensPins    = [14,15,18]
SensValues  = [0,0,0]
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

for pin in SensPins:
    GPIO.setup(pin,GPIO.IN)
  
# Define advanced Sequence
# as shown in manufacturers datasheet
sequence = [
   [1,0,0,1],
   [1,0,0,0],
   [1,1,0,0],
   [0,1,0,0],
   [0,1,1,0],
   [0,0,1,0],
   [0,0,1,1],
   [0,0,0,1]
]
        
StepCount 	= len(sequence)
StepDirR 	= 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
StepDirL 	= -1;  
# Initialise variables
StepCounterL = 0
StepCounterR = 0
 
def turn_left_wheel( StepCounterL ):
	if Speed[0] > Speed[1]: 
		return False
	#LEFT PINS
	for pin in range(0,4):
		xpin=StepPinsL[pin]# Get GPIO
		if sequence[StepCounterL][pin]!=0:
		  GPIO.output(xpin, True)
		else:
		  GPIO.output(xpin, False)

	StepCounterL += -1

	# If we reach the end of the Sequence
	# start again
	if (StepCounterL >= StepCount):
		StepCounterL = 0
	if (StepCounterL < 0):
		StepCounterL = StepCount-1
	
	time.sleep(Speed[0])

	return StepCounterL
	
def turn_right_wheel( StepCounterR ):
	if Speed[0] < Speed[1]:
		return False
	for pin in range(0,4):
		xpin=StepPinsR[pin]# Get GPIO
		if sequence[StepCounterR][pin]!=0:
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)

	StepCounterR += 1


	# If we reach the end of the Sequence
	# start again
	if (StepCounterR>=StepCount):
		StepCounterR = 0
	if (StepCounterR<0):
		StepCounterR = StepCount+StepDirR
	
	time.sleep( Speed[1] )

	return StepCounterR
 
while True: 
    counter = 0
    StepCounterL = turn_left_wheel( StepCounterL )
    StepCounterR = turn_right_wheel( StepCounterR )
    # try to echo the pins
    for pin in SensPins:
       SensValues[counter] = GPIO.input( pin )
       counter = counter + 1
    counter = 0
    print SensValues
    print Sensors.getDirection()
    Sensors.setCarDirection(SensValues)
    Speed   = getattr( Sequence, Sensors.getDirection() )
    print Speed

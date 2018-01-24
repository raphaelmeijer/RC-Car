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
 
# disable warning
GPIO.setwarnings(False) 
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPinsR   = [2,3,4,17]
StepPinsL   = [27,22,10,9]
SensPins    = [14,15,18]
ButtonPins	= [26]
SensValues  = [0,0,0]
Speed       = Sequence.FORWARD
DoDrive		= False

print "SETUP: Setting up Left pins";
# Set all pins as output
for pin in StepPinsL: 
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

print "SETUP: Setting up Right pins";
# Set all pins as output
for pin in StepPinsR:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

print "SETUP: Setting up Sensor pins";
for pin in SensPins:
    GPIO.setup(pin,GPIO.IN)

print "SETUP: Setting up Button pins";
for pin in ButtonPins:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
	global StepDirL
	
	if Speed[0] == Speed[1]:
		StepDirL = -1
	elif Speed[0] > Speed[1]: 
		if( Sensors.getDirection() == "LEFT" ):
			StepDirL	= 1
		else:	
			return False
	#LEFT PINS
	for pin in range(0,4):
		xpin=StepPinsL[pin]# Get GPIO
		if sequence[StepCounterL][pin]!=0:
		  GPIO.output(xpin, True)
		else:
		  GPIO.output(xpin, False)

	StepCounterL += StepDirL

	# If we reach the end of the Sequence
	# start again
	if (StepCounterL >= StepCount):
		StepCounterL = 0
	if (StepCounterL < 0):
		StepCounterL = StepCount+StepDirL

	return StepCounterL
	
def turn_right_wheel( StepCounterR ):
	global StepDirR
	if Speed[0] == Speed[1]:
		StepDirR = 1
	if Speed[0] < Speed[1]:
		if( Sensors.getDirection() == "RIGHT" ):
			StepDirR	= -1
		else:	
			return False
	for pin in range(0,4):
		xpin=StepPinsR[pin]# Get GPIO
		if sequence[StepCounterR][pin]!=0:
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)

	StepCounterR += StepDirR

	# If we reach the end of the Sequence
	# start again
	if (StepCounterR>=StepCount):
		StepCounterR = 0
	if (StepCounterR<0):
		StepCounterR = StepCount+StepDirR

	return StepCounterR



while True: 
	if( GPIO.input( 26 ) == 0 ):
		print "DETECTED: Started the protocol"
		DoDrive = True

	if( DoDrive ):
		counter = 0
		StepCounterL = turn_left_wheel( StepCounterL )
		StepCounterR = turn_right_wheel( StepCounterR )
		# try to echo the pins
		for pin in SensPins:
			SensValues[counter] = GPIO.input( pin )
			counter = counter + 1
		counter = 0
		
		CarDirection	= Sensors.setCarDirection(SensValues)
		# check if we have to stop the car
		if( CarDirection == "STOP" ):
			break
		Speed   = getattr( Sequence, CarDirection )
		
	time.sleep( 0.0010 )

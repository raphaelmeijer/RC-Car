#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPinsR = [2,3,4,17]
StepPinsL = [27,22,10,9]

# Define speed of the wheels
Speed	= 0.0005
 
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

  
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [
   [1,0,0,1],
   [1,0,0,0],
   [1,1,0,0],
   [0,1,0,0],
   [0,1,1,0],
   [0,0,1,0],
   [0,0,1,1],
   [0,0,0,1]
]
        
StepCount 	= len(Seq)
StepDirR 	= 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
StepDirL 	= -1; 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)
 
# Initialise variables
StepCounterL = 0
StepCounterR = 0
 
 
def turnLeftWheel( StepCounterL ):
	#LEFT PINS
	for pin in range(0,4):
		xpin=StepPinsL[pin]# Get GPIO
		if Seq[StepCounterL][pin]!=0:
		  print " Enable GPIO %i" %(xpin)
		  GPIO.output(xpin, True)
		else:
		  GPIO.output(xpin, False)

	StepCounterL += StepDirL

	# If we reach the end of the sequence
	# start again
	if (StepCounterL>=StepCount):
		StepCounterL = 0
	if (StepCounterL<0):
		StepCounterL = StepCount+StepDirL

	return StepCounterL
	
def turnRightWheel( StepCounterR ):
	for pin in range(0,4):
		xpin=StepPinsR[pin]# Get GPIO
		if Seq[StepCounterR][pin]!=0:
			print " Enable GPIO %i" %(xpin)
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)

	StepCounterR += StepDirR

 
	# If we reach the end of the sequence
	# start again
	if (StepCounterR>=StepCount):
		StepCounterR = 0
	if (StepCounterR<0):
		StepCounterR = StepCount+StepDirR
	
	return StepCounterR
 
# Start main loop
while True:
  StepCounterL = turnLeftWheel( StepCounterL )
  StepCounterR = turnRightWheel( StepCounterR )
 
  # Wait before moving on
  time.sleep(Speed)

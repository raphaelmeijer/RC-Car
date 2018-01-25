#!/usr/bin/python
# Import required libraries
import os, random
import pyttsx
import sys
import time
from Sensors import Sensors
from Sequence import Sequence
from Speech import Speech
# import led
import RPi.GPIO as GPIO

 
# Init classes 
Sensors     = Sensors()
Sequence    = Sequence()
Speech		= Speech()

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
LedPins 	= [5, 6, 13, 19, 20, 21]
ButtonPins	= [26, 12]
SensValues  = [0,0,0]
AllowedToDrive       		= Sequence.FORWARD
DoDrive						= False
previous_front_button_state	= False
front_button_counter		= 3
message 					= ""
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

print "SETUP: Setting up LED pins";
# Set all pins as output
for pin in LedPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, True)
  
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
StepDirR 	= 1 	# Set to 1 or 2 for clockwise
StepDirL 	= -1;  	# Set to -1 or -2 for anti-clockwise
StepCounterL = 0	# Will indicate the order later
StepCounterR = 0	# Will indicate the order later

# The left wheel will have it's own function
def turn_left_wheel( StepCounterL ):
	# We need the global var, otherwise it will reset always
	global StepDirL
	
	# Check the direction of the wheel
	if AllowedToDrive[0] and AllowedToDrive[1] or AllowedToDrive[0]:
		# if have have the wheels, go front! ( the left wheel is a right wheel, so we have to do it in reverse )
		StepDirL = -1
	elif AllowedToDrive[0] == False : 
		# if we don't have the left wheel
		if( Sensors.getDirection() == "LEFT" ):
			# and we wanna go a sharp left, set to back
			StepDirL	= 1
		else:	
			# otherwise, stop the wheel! - for a slow turn
			return False
			
	# Loop through the left wheel pins
	for pin in range(0,4):
		xpin = StepPinsL[pin] # Get correct GPIO pin number
		if sequence[StepCounterL][pin] != 0: # the pin is the same as the sequence we need
		  GPIO.output(xpin, True)	# if it is higher than 0, we can activate the pin
		else:
		  GPIO.output(xpin, False) 	# if it is lower than 1, we can deactivate the pin

	# increment the step counter with the step in the correct direction
	StepCounterL += StepDirL

	# If we reach the end of the Sequence
	# start again
	if (StepCounterL >= StepCount):
		StepCounterL = 0
	if (StepCounterL < 0):
		StepCounterL = StepCount+StepDirL

	# return the counter
	return StepCounterL
	
def turn_right_wheel( StepCounterR ):
	# We need the global var, otherwise it will reset always
	global StepDirR
	
	if ( AllowedToDrive[0] and AllowedToDrive[1] ) or AllowedToDrive[1]:
		# if have have the wheels, go front! ( the left wheel is a right wheel, so we have to do it in reverse )
		StepDirR = 1
	if AllowedToDrive[1] == False:
		# if we don't have the right wheel
		if( Sensors.getDirection() == "RIGHT" ):
			# and we wanna go a sharp left, set to back
			StepDirR	= -1
		else:	
			# otherwise, stop the wheel! - for a slow turn
			return False
	# Loop through the left wheel pins
	for pin in range(0,4):
		xpin = StepPinsR[pin] # Get correct GPIO pin number
		if sequence[StepCounterR][pin] != 0: # the pin is the same as the sequence we need
			# if it is higher than 0, we can activate the pin
			GPIO.output(xpin, True)	
		else:
			# if it is lower than 1, we can deactivate the pin
			GPIO.output(xpin, False) 	

	# increment the step counter with the step in the correct direction
	StepCounterR += StepDirR

	# If we reach the end of the Sequence
	# start again
	if (StepCounterR>=StepCount):
		StepCounterR = 0
	if (StepCounterR<0):
		StepCounterR = StepCount+StepDirR

	return StepCounterR
while True: 
	current_front_button_state = GPIO.input(12)
	if ( current_front_button_state != previous_front_button_state and current_front_button_state == 0 ):  
		# we have to reset the counter
		if( front_button_counter >= 4 ):
			front_button_counter = 1
		else:
			front_button_counter  = front_button_counter + 1  # always increment
		# ask for verification
		if( front_button_counter % 4 == 0 ):
			print "NOTICED: We have selected Nothing"
			# No destination
			Sensors.hasDestination = ""
			# Let the user know that we have no destination
			message ="Current direction: No direction"			
		elif( front_button_counter % 3 == 0 ):
			print "NOTICED: We have selected C"
			# go to C
			Sensors.hasDestination 	= "C"
			# Let the user know that we have the right destination
			message 				= "You have chosen: Right"
		elif( front_button_counter % 2 == 0 ):
			print "NOTICED: We have selected B"
			# go to B
			Sensors.hasDestination 			= "B"
			# Let the user know that we have the straight destination
			message 						= "You have chosen: straight"
		elif( front_button_counter % 1 == 0 ):
			print "NOTICED: We have selected A";
			Sensors.hasDestination 			= "A"
			# Let the user know that we have left destination
			message 						= "You have chosen: left"
		Speech.speak(message)
	# check if we have a clicked input
	if( GPIO.input( 26 ) == 0 ):
		# let us know we are starting!
		print "DETECTED: Started the protocol"
		# count down!
		Speech.count_of()
		# motor sound after count down
		Speech.play_motor_sound()
		# open the file 
		f 						= open('end_destination.txt','r') 
		# get destination	
		destination 			= f.read() 
		if( destination != "" ):
			# set destination
			Sensors.hasDestination	= destination 
			print "Chosen destination: %s" % destination
		# start variable
		DoDrive = True
	
	# only do this code if we want to start	
	if( DoDrive ):
		counter 		= 0 # we need a counter for the sens values
		StepCounterL 	= turn_left_wheel( StepCounterL ) # turn the left wheel
		StepCounterR 	= turn_right_wheel( StepCounterR ) # turn the right wheel
		# Loop through the sensor pins
		for pin in SensPins:
			SensValues[counter] = GPIO.input( pin ) # get the input from the GPIO ( 1 or 0 )
			counter 			= counter + 1 # incerement the counter
		counter = 0 # reset the counter after the loop
		# get the car direction from the sensors class
		CarDirection	= Sensors.setCarDirection(SensValues)
		# check if we have to stop the car
		if( CarDirection == "STOP" ):
			# let the user know we have arrived at the destination
			Speech.speak("You have reached your destination: " + Sensors.hasDestination) 
			# break the loop and end the script
			break
		# get which wheel is allowed to drive
		AllowedToDrive   = getattr( Sequence, CarDirection )
	#set previous button
	previous_front_button_state = current_front_button_state  
	# sleep temporarily
	time.sleep( 0.0010 )  
	
# clean the GPIO 
print "Cleaning up GPIO"
GPIO.cleanup()
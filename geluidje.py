#!/usr/bin/env python
import os, random

def rndmp3 ():
	randomfile = random.choice(os.listdir("/home/pi/music/"))
	file = ' /home/pi/music/'+ randomfile
	os.system ('mplayer' + file)


# global variables
buttonPin = 26  # this will be an input pin to which the button is attached
				# in this case pin GPIO23 (which is pin number 16)
prev_state = 1  # set start state to 1 (button released)

# we're using the BCM pin layout of the Raspberry PI
GPIO.setmode(GPIO.BCM)

# set pin GPIO23 to be an input pin; this pin will read the button state
# activate pull down for pin GPIO23
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


############
# Run code #
############

# initialize event
event = 1

print "Klik op de knop om een geluidje af te spelen"

# keep on executing this loop forever (until someone stops the program)
while True:

	# read the current button state by reading pin GPIO23 on the Raspberry PI
	# the curr_state can be '0' (if button pressed) or '1' (if button released)
	curr_state = GPIO.input(buttonPin)

	# if state changed, take some actions
	if (curr_state != prev_state):  # state changed from '1' to '0' or from '0' to '1'
		if (curr_state == 1):  # button changed from pressed ('0') to released ('1')
			event = "released"
			print event  # print event to console
		else:   # button changed from released ('1') to pressed ('0')
			event = "pressed"  # print event to console
			print event
			rndmp3 ()
		prev_state = curr_state  # store current state

	time.sleep(0.02)  # sleep for a while, to prevent bouncing

# when exiting, reset all pins
GPIO.cleanup()
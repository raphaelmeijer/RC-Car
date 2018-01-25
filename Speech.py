import os, random
import pyttsx
import time
import RPi.GPIO as GPIO

class Speech:
	engine 		= False # we will store the sound engine in this variable
	count_from 	=  3 	# we will count from 3
	
	def __init__( self ):
		# initiate the sound engine
		self.engine 	= pyttsx.init()
		# set the volume of the engine
		self.engine.setProperty( 'volume', 12)
	def play_motor_sound ( self ):
		# the file to play
		file = ' /home/pi/music/"motor.mp3" '
		# let the OS to play the file
		os.system ('omxplayer ' + file)
	#starting countdown when pressing button 	
	def count_of( self ):
		# loop through from count
		while (self.count_from > 0): 
			# let the user know on which count we are
			self.speak(self.count_from)
			# we need 1 less
			self.count_from = self.count_from - 1 
	def speak( self, message ):
		print "Said: %s" % message
		# tell the user what we want to say
		self.engine.say( message )
		# run the engine and wait for it to finish
		self.engine.runAndWait()
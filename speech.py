class talk:
	import os, random
	import pyttsx
	import time
	import RPi.GPIO as GPIO

	#engine sound
	def Starting_sound ():
		file = ' /home/pi/music/"motor.mp3" '
		os.system ('omxplayer' + file)
	#starting countdown when pressing button 	
	def aftellen():
		count = 3
		while (count > 0): 
			engine = pyttsx.init()
			engine.setProperty( 'volume', 12)
			engine.say(count)
			engine.runAndWait()
			count = count -1
			print count
			
			
	message = "  "
	def talkBack(message):
		# text to speech engine 
		engine = pyttsx.init()
		engine.setProperty( 'volume', 12)
		engine.say(message)
		engine.runAndWait()

	
	def messageStart():	
		engine = pyttsx.init()
		engine.setProperty( 'volume', 12)
		engine.say("Press the button on the Front to make a choice which way to go, then press the button on the back to start the engines")
		engine.runAndWait()

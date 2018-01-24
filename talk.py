class talk:

	import os, random
	import pyttsx
	import time
	import RPi.GPIO as GPIO


	def aftellen():
		count = 3
		while (count > 0): 
			engine = pyttsx.init()
			engine.say(count)
			engine.runAndWait()
			count = count -1
			print count

			time.sleep(1) 
		
	def spraak():
			engine = pyttsx.init()
			engine.say("begin")
			engine.runAndWait()
			
	def R2D2Random ():
		randomfile = random.choice(os.listdir("/home/pi/music/"))
		file = ' /home/pi/music/+ randomfile'
		os.system ('omxplayer' + file)
		
	def sandstorm ():
		file = ' /home/pi/songs/sandstorm.mp3'
		os.system ('omxplayer' + file)
		
	count_Pressed = 0;
		
	buttonPin = 26  
					
	prev_state = 1  

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


	############
	# Run code #
	############

	event = 1	

	print "Klik op de knop om een geluidje af te spelen"

	while True:


		curr_state = GPIO.input(buttonPin)


		if (curr_state != prev_state):  
			if (curr_state == 1):  
				event = "released"
				print event  
				
			else:   
				event = "pressed"
				print event
				
				count_Pressed = count_Pressed + 1
				
				aftellen()
				spraak()	
				sandstorm()
				print "HIERHIERHIERHIERHIERHIERHIERHIERHIERHIERHIERHIERHIERHI"
				
				if (count_Pressed > 1):  
					os.system(" killall -g omxplayer ")
					break
					
			
			prev_state = curr_state  

		time.sleep(0.02)  

	GPIO.cleanup()
		
		

		

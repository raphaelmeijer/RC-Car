


import pyttsx
import time

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
		
		

		

aftellen()
spraak()
sandstorm()
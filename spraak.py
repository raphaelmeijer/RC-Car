


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
		
		

		

aftellen()
spraak()
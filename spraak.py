class Aftellen


import pyttsx
count = 3
import time

def aftellen()
	while (count > 0): 
		engine = pyttsx.init()
		engine.say(count)
		engine.runAndWait()
		count = count -1
		print count

	time.sleep(1) 
	
aftellen()
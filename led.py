import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

while (True):
	GPIO.output(5,True)
	GPIO.output(6,True)
	GPIO.output(13,True)
	GPIO.output(19,True)
	GPIO.output(20,True)
	GPIO.output(21,True)
	time.sleep(1)
	
GPIO.cleanup()
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
	time.sleep(1)
	GPIO.output(5,False)
	GPIO.output(6,True)
	time.sleep(1)
	GPIO.output(6,False)
	GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(13,False)
	GPIO.output(19,True)
	time.sleep(1)
	GPIO.output(19,False)
	GPIO.output(20,True)
	time.sleep(1)
	GPIO.output(20,False)
	GPIO.output(21,True)
	time.sleep(1)
	GPIO.output(21,False)
	time.sleep(1)
	
GPIO.cleanup()
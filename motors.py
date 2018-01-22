import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 2
Motor1B = 3
Motor1C = 4
Motor1D = 17

Motor2A = 27
Motor2B = 22
Motor2C = 10
Motor2D = 9


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1C,GPIO.OUT)
GPIO.setup(Motor1D,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2C,GPIO.OUT)
GPIO.setup(Motor2D,GPIO.OUT)

print "Going forwards"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1C,GPIO.LOW)
GPIO.output(Motor1D,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2C,GPIO.LOW)
GPIO.output(Motor2D,GPIO.HIGH)

sleep(0,02)
 
print "Going backwards"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1C,GPIO.HIGH)
GPIO.output(Motor1D,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2C,GPIO.HIGH)
GPIO.output(Motor2D,GPIO.HIGH)
 
sleep(0,02)

print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
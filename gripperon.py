from time import sleep
import RPi.GPIO as GPIO

def gripperon():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)

	suction1 = 05 
	suction2 = 06
	enable = 17
	
	GPIO.setup(suction1, GPIO.OUT)
	GPIO.setup(suction2, GPIO.OUT)
	GPIO.setup(enable, GPIO.OUT)

	GPIO.output(suction1,GPIO.LOW)
	GPIO.output(suction2,GPIO.HIGH)
	GPIO.setup(enable, GPIO.HIGH)

def gripperoff():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)

	suction1 = 05 
	suction2 = 06
	enable = 17
	
	GPIO.setup(suction1, GPIO.OUT)
	GPIO.setup(suction2, GPIO.OUT)
	GPIO.setup(enable, GPIO.OUT)

	GPIO.output(suction1,GPIO.LOW)
	GPIO.output(suction2,GPIO.HIGH)
	GPIO.setup(enable, GPIO.LOW)

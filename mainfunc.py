import numpy as np
import cv2
import picamera
import RPi.GPIO as GPIO
import imutils
from time import sleep
from angle import turn_45, turn_90, turn_180
from calcdist import calcdistance
from clickpicture import click
from detect import detectball, detectscreen
from dist import move_forward
from gripperon import gripperon, gripperoff
from maskandedged import mask, edged

def mainfunc(state, count):
	colours = ('red', 'blue')
	if count > 1:
		return
	
	if state > 360:
		return mainfunc(0, count + 1)
	for colour in colours:
		click()
		msk = mask(colour)
		ball = detectball(msk)
		if ball != []:
			d = calcdistance(ball[1])
			print(d)
	
			move_forward(d/100)
	
			gripperon()
			sleep(5)
			
			turn_45()
			sleep(2)
	
			click()
			print "screen clicked"
			eged = edged(colour)
			screen = detectscreen(eged)
			#print(screen)
			angle =0
			#msk = mask(colour)
			#eged = edged(colour)
			while screen == 0 and angle<360:
				angle = angle + 45
				turn_45()
				sleep(2)
	
				click()
				egeed = edged(colour)
				screen = detectscreen(egeed)
			if angle >= 360:
				print "no screen detected"
				return
			print(screen)
			e = calcdistance(screen)
			move_forward(e/100)
			gripperoff()
			sleep(3)
			turn_180()
			return mainfunc(0, 0)
	
		print "no" + colour "ball detected"
	
	turn_45()
		
	return mainfunc(state + 45, count)
	
	GPIO.cleanup()

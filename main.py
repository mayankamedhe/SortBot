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
from mainfunc import mainfunc

print "imported"
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

Motor1A = 16
Motor1B = 12
Motor1E = 04
Motor2A = 26
Motor2B = 19
Motor2E = 18
suction1 = 05 
suction2 = 06
enable = 17
	
GPIO.setup(suction1, GPIO.OUT)
GPIO.setup(suction2, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

state = 0
count = 0

mainfunc(state, count)
		

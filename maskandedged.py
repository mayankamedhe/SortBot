import numpy as np
import cv2
import imutils
kernel = np.ones((9,9),np.uint8)
def mask(colour):
	lower = {'red':(155,50,0), 'blue':(80, 100, 10), 'green':(60,40,10)} 
	upper = {'red':(185,225,160), 'blue':(110,220,190), 'green':(95,215,120)}
	
	image = cv2.imread('img.jpg', 1)
	image = imutils.resize(image, width=600)

	blurred = cv2.GaussianBlur(image, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	for x in range(397):
		for y in range(597):
			if x+y>710:
				hsv[x][y] = [0,0,0]

	#kernel = np.ones((9,9),np.uint8)
        	
	mask = cv2.inRange(hsv, lower[colour], upper[colour])
	
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	return cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

def edged(colour):
	lower = {'red':(155,50,0), 'blue':(80, 100, 10), 'green':(60,40,10)} 
	upper = {'red':(185,225,160), 'blue':(110,220,190), 'green':(95,215,120)}
	print "1"
	image = cv2.imread('img.jpg', 1)
	print "2"
	image = imutils.resize(image, width=600)
	print "3"
	blurred = cv2.GaussianBlur(image, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	print "4"
	for x in range(397):
		for y in range(597):
			if x+y>710:
				hsv[x][y] = [0,0,0]

	#kernel = np.ones((9,9),np.uint8)
        print "5"
	mask = cv2.inRange(hsv, lower[colour], upper[colour])
	print "6"	
	edged = cv2.Canny(mask,10,200)	
	print "7"
	edged = cv2.morphologyEx(edged, cv2.MORPH_OPEN, kernel)
	print "8"
	return cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

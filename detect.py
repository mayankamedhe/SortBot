import numpy as np
import cv2
import imutils

def detectball(mask):
	cnts = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
			       
	if len(cnts) > 0:
	       	c = max(cnts, key=cv2.contourArea)
	       	((x, y), radius) = cv2.minEnclosingCircle(c)
	       	M = cv2.moments(c)
	       	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	       	if radius > 0.5 and radius < 52 and y > 100:
			return [int(x), int(y)]
	return []

def detectscreen(edged):
	cnts1 = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
	
	for b in cnts1:
		peri = cv2.arcLength(b, True)
		area1 = cv2.contourArea(b)
		rect = cv2.minAreaRect(b)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		area2 = cv2.contourArea(box)
		approx = cv2.approxPolyDP(b, 0.02 * peri, True)
		if len(approx) == 4 and area1 > 250 and abs(area1 - area2) < 1000:	
			lowermid = max(approx[0][0][1],approx[2][0][1],approx[1][0][1],approx[3][0][1])
			return lowermid
	return 0


import numpy as np
import imutils
import cv2
#import picamera

lower = {'red':(155,50,0), 'blue':(80, 100, 10), 'green':(60,40,10)}
upper = {'red':(185,225,160), 'blue':(110,220,190), 'green':(95,215,120)}

colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0)}

#camera = picamera.PiCamera()
#camera.brightness = 50    # brightness can be adjusted according to requirement 
#camera.capture('img.jpg')
image = cv2.imread('img.jpg', 1) 
frame = imutils.resize(image, width=600)

blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)



for x in range(400):
	for y in range(597):
		if x+y>704:
			hsv[x][y] = [0,0,0]

#cv2.imshow("hsv", frame)
#cv2.imshow("hsv", hsv)
#cv2.waitKey(0)

    #for each color in dictionary check object in frame
for key, value in upper.items():
     	# construct a mask for the color from dictionary`1, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
	edged = cv2.Canny(mask, 10, 200)
	#fra = imutils.resize(mask, width=600)
	#frad = imutils.resize(edged, width=600)
	#print(key)	
#	cv2.imshow("mask",mask)
#	cv2.waitKey(0)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	edged = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        edged = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#	cv2.imshow("edged",edged)
#	cv2.waitKey(0)
               
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        center = None
	_, cnts1, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		       
        # only proceed if at least one contour was found
	if len(cnts) > 0:     
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
       
            # only proceed if the radius meets a minimum size. Correct this value for your object's size
            if radius > 0.5 and radius < 52 and y > 100:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                #cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 1)
                #cv2.putText(frame,key + " ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
		print(y)
		        
	for b in cnts1:
		peri = cv2.arcLength(b, True)
		area1 = cv2.contourArea(b)
		rect = cv2.minAreaRect(b)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		area2 = cv2.contourArea(box)
		approx = cv2.approxPolyDP(b, 0.02 * peri, True)

		if len(approx) == 4 and area1 > 250 and abs(area1 - area2) < 1000:
#this 100000 can also be changed. it is the difference between the areas of the shape and its enclosing rectangle. if difference is lesser than a certain value then shape is a rectangle. the 2000 can also be changed, it is the min area the rectangle must have to get detected, its there to remove the arbit noise.
		#print(area1)
			print(area2, peri)
			cv2.drawContours(frame, [approx], -1, colors[key], 4)
			cv2.putText(frame,key + " rectangle", tuple(box[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],10)
     
    # show the frame to our screen
#fra = imutils.resize(frame, width=600)
#cv2.imshow("Frame", frame)
   
#cv2.waitKey(0)
 
# cleanup the camera and close any open windows

cv2.destroyAllWindows()

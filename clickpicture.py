import picamera
camera = picamera.PiCamera()
def click():
	camera.brightness = 50
	camera.capture('img.jpg')

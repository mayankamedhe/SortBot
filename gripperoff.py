def gripperon():
	GPIO.output(suction1,GPIO.LOW)
	GPIO.output(suction2,GPIO.HIGH)
	GPIO.setup(enable, GPIO.LOW)

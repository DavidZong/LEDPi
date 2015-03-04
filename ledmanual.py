## This program allows for the manual on off of the LEDs

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
	print "Enter command: "
	print "on, off or quit"
	next = raw_input("> ")
	if next == "quit":
		GPIO.output(11, False)
		break
	elif next == "on":
		GPIO.output(11, True)
	elif next == "off":
		GPIO.output(11, False)
	else:
		print "Please enter valid command"

GPIO.cleanup()
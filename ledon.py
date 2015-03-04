import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

print "Turning On"
while True:
	try:
		GPIO.output(11, True)
		sleep(30)
		print "Turning off"
		GPIO.output(11, False)
		sleep(30)
		print "Turning On"
	except KeyboardInterrupt

GPIO.cleanup()
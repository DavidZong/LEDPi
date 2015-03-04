import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    GPIO.output(11, True)
    sleep(2)
    GPIO.output(11, False)
    sleep(2)
    print "Running, press ctrl+Z to quit"
    

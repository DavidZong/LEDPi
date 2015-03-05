# This script allows the user to choose between a list of periodic functions and
# make the LED shine light in that manner

## Import packages
import time
import RPi.GPIO as GPIO
import numpy as np

## Define GPIO pins and set the GPIO out pin to 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


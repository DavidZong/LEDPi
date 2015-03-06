# This script allows the user to choose between a list of periodic functions and
# make the LED shine light in that manner

## Import packages
import time
import RPi.GPIO as GPIO
import numpy as np

## Define GPIO pins and set the GPIO out pin to 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

## show user menu that lets them choose how to define function

## get math function from user as a function of time

## run LED program until user stops
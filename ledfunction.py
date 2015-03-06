# This script allows the user to choose between a list of periodic functions and
# make the LED shine light in that manner

## Import packages
import time
import RPi.GPIO as GPIO
import numpy as np
from ledFunctionGen import sineGen, squareGen, triGen, sawGen, customGen
from sys import exit

## Define GPIO pins and set the GPIO out pin to 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

## show user menu that lets them choose how to define function
def menu():
	print "Welcome to the LEDPi"
	print "Please select function option or Q to quit"
	print "1. Sine\n2. Square\n3. Triangle\n4. Sawtooth\n5. Custom"
	# loop user input
	next = raw_input("> ")
	while True:
		if next == "1":
			sineGen()
		elif next == "2":
			squareGen()
		elif next == "3":
			triGen()
		elif next == "4":
			sawGen()
		elif next == "5":
			customGen()
		elif next == "q":
			print "Quitting..."
			GPIO.cleanup()
			sys.exit()
		else:
			print "Please enter a valid option"
			print "1. Sine\n2. Square\n3. Triangle\n4. Sawtooth\n5. Custom"
			next = raw_input("> ")
	
## run LED program until user stops
## runLED(function) takes an array and sends that as greyscale PWM to the GPIO pins. Upon reaching the end of
## the array, the function should loop the array until the user tells the program to stop. The PWM frequency
## should be set to 1000 Hz. LATER: build functionality for a timer
def runLED(function):


## Run the program
menu()

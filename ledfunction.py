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
		else:
			print "Please enter a valid option"
			print "1. Sine\n2. Square\n3. Triangle\n4. Sawtooth\n5. Custom"
			next = raw_input("> ")
	

## get math function from user as a function of time and generate an array with 1 ms resolution:
## functions in this family are sineGen(), squareGen(), triGen(), sawGen() and customGen()

## sineGen() accepts no parameters and outputs an array of values that define greyscale PWM values
## of a sine wave. This function should take user input of amplitude, period, min value and max value.
## the array this method generates should be one full period of a sine wave. 
def sineGen():
	print "Not Implemented Yet!"
	return []

def squareGen():
	print "Not Implemented Yet!"
	return []

def triGen():
	print "Not Implemented Yet!"
	return []

def sawGen():
	print "Not Implemented Yet!"
	return []

## customGen() asks the user to point it to a csv file that represents an array of PWM values. This csv
## can be anything. The csv must be 1 dimentional, and each cell represents 1 ms 
def customGen():
	print "Not Implemented Yet!"
	return []

## run LED program until user stops
## runLED(function) takes an array and sends that as greyscale PWM to the GPIO pins. Upon reaching the end of
## the array, the function should loop the array until the user tells the program to stop. The PWM frequency
## should be set to 1000 Hz. LATER: build functionality for a timer
def runLED(function):


## the main method
def main():
	# some while loop or something

## run the program
main()
GPIO.cleanup()
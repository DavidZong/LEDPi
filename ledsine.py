## This program makes the LEDs oscillate in a user defined
## sinusoid. One can select the period and the amplitude

## Import packages
import time
import RPi.GPIO as GPIO
import numpy as np

## Define GPIO pins and set the GPIO out pin to 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

## Ask the user for parameters and returs them as an
def getParams():
	params = []
	print("Enter desired period (seconds)")
	period = getNumber()
	print("Enter desired amplitude (1-50)")
	amplitude = getNumber()
	params.append(period)
	params.append(amplitude)
	return params

## This method asks the user for a number until the user inputs
## a number. Then it returns that number as a float.
def getNumber():
	next = raw_input("> ")
	while True:
		if next.isdigit():
			nextNum = float(next)
			break
		else:
			print "Please enter an integer"
			next = raw_input("> ")
	return nextNum

## This function makes the PWM sinusioid until the user aborts
def generateSine(period, amplitude):
	p = GPIO.PWM(11, 60)
	p.start(0)
	print("Generating sine wave...")
	print("Press CTRL+C to abort")
	pi = np.pi
	x = np.linspace(pi, 3*pi, 101)
	y = amplitude*(1 + np.sin(x))
	count = 0
	try:
		startTime = time.time()
		while True:
			for i in xrange(1, 101):
				p.ChangeDutyCycle(y[i-1])
				time.sleep(period / 101)
				#print(y[i-1]) # Uncomment this to debug amplitude issues
			# Uncomment below to debug timing issues
			#print(count)
			#count = count + 1
			#currentTime = round(time.time() - startTime)
			#print("Time elapsed: " + str(currentTime) + " seconds")
	except KeyboardInterrupt:
		pass
		
		
# This is the main method
def main():
	params = getParams()
	generateSine(params[0], params[1])
	print("\n" + "User aborted sequence")
	GPIO.cleanup()

# Run the program
main()

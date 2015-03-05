# LEDPi: LED Control with RPi

This repository contains some scripts to control an LED with a Raspberry Pi. Requires RPi.GPIO and some scripts need numpy.

Currently, all files are basic Python scripts.

My goal with this is to write an actual piece of command line software that does full PWM control of a single LED or LED array.
Here is a list of desired functionalities:
 - 100 levels of greyscale control
 - full arbitrary function generation
 - non-continuous function generation
 - CSV table based numeric function definition
	- this is probably the easiest way to do arbitrary functions, but it's less robust
 - parametric function definition (for multiple functions)
	- more robust, but harder to implement for all functions, especially non-continuous
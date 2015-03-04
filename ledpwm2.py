import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 100)
p.start(0)
input = 0
while input != "q":
    input = raw_input("Enter desired brightness (1 - 100) or q to quit ")
    if input == "q":
        break
    while not input.isdigit() and input != "q":
        print("Not valid, try again")
        input = raw_input(">> ")
    while float(input) > 100 or float(input) < 1:
        print("Not valid value, enter a number 1 - 100 ")
        input = raw_input(">> ")
        if not input.isdigit():
            print("Not valid, try again")
            break
    if input.isdigit():
        dc = float(input)
        p.ChangeDutyCycle(dc)
p.stop()
GPIO.cleanup()
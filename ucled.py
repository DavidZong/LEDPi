import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

speed = raw_input("Enter PWM frequency: ")
p = GPIO.PWM(11, float(speed))
dc = raw_input("Enter Duty Cycle: ")
p.ChangeDutyCycle(float(dc))
p.start(1)
raw_input("Press enter to stop")
p.stop()
GPIO.cleanup()

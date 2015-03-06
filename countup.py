## A program that counts fast
import time
x = 0
startTime = time.time()
while True:
	print x
	x = x + 1
	if (x % 1000) == 0:
		currentTime = round(time.time() - startTime)
		print currentTime
	time.sleep(0.001)
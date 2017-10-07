import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(4,IO.OUT)
IO.setup(5,IO.OUT)
IO.setup(6,IO.OUT)
x=1

while 1:
	for y in range(8):
		IO.output(4,1)
		time.sleep(0.1)
		IO.output(5,1)
		time.sleep(0.1)
		IO.output(5,0)
		IO.output(4,0)
		IO.output(6,1)
		time.sleep(0.1)
		IO.output(6,0)

	for y in range(8):
		IO.output(4,0)
		time.sleep(0.1)
		IO.output(5,1)
		time.sleep(0.1)
		IO.output(5,0)
		IO.output(4,0)
		IO.output(6,1)
		time.sleep(0.1)
		IO.output(6,0)


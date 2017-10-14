import RPi.GPIO as GPIO
import RPiShift
import time
GPIO.setwarnings(False)
'''
IO.setmode(IO.BCM)
IO.setup(4,IO.OUT) #Data
IO.setup(5,IO.OUT) #Clock
IO.setup(6,IO.OUT) #latch
'''
shift = RPiShift.Shifter(4, 5, 6, 1, GPIO.BCM)
x=1

OFF  = 0x00
A = LED1 = 0x01
B = LED2 = 0x02
C = LED3 = 0x04
D = LED4 = 0x08
E = LED5 = 0x10
F = LED6 = 0x20
G = LED7 = 0x40
H = LED8 = 0x80

while 1:
	shift.writeByte(A)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(B)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(C)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)

'''
while 1:
	for y in range(8):
		IO.output(4,1)
		IO.output(5,1)
		IO.output(5,0)
		IO.output(4,0)
		IO.output(6,1)
		time.sleep(0.3)
		IO.output(6,0)

	for y in range(8):
		IO.output(4,0)
		IO.output(5,1)
		IO.output(5,0)
		IO.output(4,0)
		IO.output(6,1)
		time.sleep(0.3)
		IO.output(6,0)
'''


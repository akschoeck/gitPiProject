import RPi.GPIO as GPIO
import RPiShift
import time
GPIO.setwarnings(False)
shift = RPiShift.Shifter(4, 18, 17, 1, GPIO.BCM)
shift2 = RPiShift.Shifter(27, 23, 22, 1, GPIO.BCM)
x=1

OFF  = 0x00
A = LED1  = 0x01
B = LED2  = 0x02
C = LED3  = 0x04
D = LED4  = 0x08
E = LED5  = 0x10
F = LED6  = 0x20
G = LED7  = 0x40
H = LED8  = 0x80

I = LED9  = 0x01
J = LED10 = 0x02
K = LED11 = 0x04
L = LED12 = 0x08
M = LED13 = 0x10
N = LED14 = 0x20
O = LED15 = 0x40
P = LED16 = 0x80

Q = LED17 = GPIO.output(25, GPIO.HIGH)
R = LED18 = GPIO.output(5, GPIO.HIGH)
S = LED19 = GPIO.output(12, GPIO.HIGH)
T = LED20 = GPIO.output(6, GPIO.HIGH)
U = LED21 = GPIO.output(13, GPIO.HIGH)
V = LED22 = GPIO.output(16, GPIO.HIGH)
W = LED23 = GPIO.output(19, GPIO.HIGH)
Y = LED24 = GPIO.output(20, GPIO.HIGH)
X = LED25 = GPIO.output(26, GPIO.HIGH)
Z = LED26 = GPIO.output(21, GPIO.HIGH)


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
	shift.writeByte(D)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(E)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(F)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(G)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(H)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(I)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(J)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(K)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(L)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(M)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(N)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(O)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	shift.writeByte(P)
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	Q
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	R
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	S
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	T
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	U
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	V
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	W
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	X
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	Y
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
	Z
	time.sleep(1)
	shift.writeByte(OFF)
	time.sleep(1)
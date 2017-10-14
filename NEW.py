import RPi.GPIO as GPIO
import time

SDI   = 4 #Data
RCLK  = 5 #Latch
SRCLK = 6 #Clock

def print_msg():
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)

	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)

	for i in range(16, 27):
		GPIO.setup(i, GPIO.OUT)
		
def loop():

	while True:

		#4 Data
		#5 Clock
		#6 Latch

		print('LED 3 is about to turn on')

		time.sleep(1)

		GPIO.output(6, GPIO.HIGH) #Latch on

		GPIO.output(5, GPIO.HIGH) #LED 1
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 2
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 3
		GPIO.output(4, GPIO.HIGH)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 4
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 5
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 6
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 7
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 8
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(6, GPIO.LOW) #Latch off

		time.sleep(1)

		print('LED 3 is about to turn off')
		
		time.sleep(1)

		GPIO.output(6, GPIO.HIGH) #Latch on

		GPIO.output(5, GPIO.HIGH) #LED 1
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 2
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 3
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 4
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 5
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 6
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 7
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(5, GPIO.HIGH) #LED 8
		GPIO.output(4, GPIO.LOW)
		GPIO.output(5, GPIO.LOW)

		GPIO.output(6, GPIO.LOW) #Latch off
		
		time.sleep(1)


def destroy():   # When program ending, the function is executed. 
	GPIO.cleanup()

if __name__ == '__main__': # Program starting from here 
	print_msg()
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)

try:
  while True:
	  GPIO.output(21, 0)
	  time.sleep(5)
	  GPIO.output(21, 1)
	  time.sleep(5)
except KeyboardInterrupt():
  GPIO.cleanup()
  

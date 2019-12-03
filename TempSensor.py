import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

promt = ""
for i in range(10):
    data = GPIO.input(21)
    print(data)
    time.sleep(0.1)
GPIO.cleanup()




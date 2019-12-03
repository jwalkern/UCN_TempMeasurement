import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

promt = ""
while promt != 'q':
    promt = input("tast 'q' for quit: ")
    data = GPIO.input(17)
    print(data)
    time.sleep(1)
GPIO.cleanup()




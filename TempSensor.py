import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

promt = ""
for i in range(10):
    data = MCP3008(channel=4,device=1)
    print(data)
    time.sleep(0.1)
GPIO.cleanup()




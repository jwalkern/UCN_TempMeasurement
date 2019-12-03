import time
from gpiozero import MCP3008

for i in range(0):
    data = MCP3008(channel=4, device=1)
    print(data)
    time.sleep(0.1)
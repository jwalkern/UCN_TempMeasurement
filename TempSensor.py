import time
from gpiozero import MCP3008

for i in range(10):
    data = MCP3008(port=4, device=1)
    print(data)
    time.sleep(0.1)
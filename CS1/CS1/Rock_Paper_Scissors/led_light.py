import random
import time
import sys

rgb = [f'\033[32m[{"red"},{"green"},{"blue"}\033[m']

while True:
    led = random.choice(rgb)
    print(f"\n{led}")
    time.sleep(2)
    
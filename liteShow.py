import time
import random
from piglow import PiGlow

# Colour = pi.colour (1-6, 0-255) W,B,G,Y,O,R
# White  = pi.white  (0-255)
# Blue   = pi.blue   (0-255)
# Green  = pi.green  (0-255)
# Yellow = pi.yellow (0-255)
# Orange = pi.orange (0-255)
# Red    = pi.red    (0-255)
# All    = pi.all    (0-255)
# LED    = pi.led    (1-18, 0-255)
# Arm    = pi.arm    (1-3, 0-255
# Arm 1  = pi.arm1   (0-255)
# Arm 2  = pi.arm2   (0-255)
# Arm 3  = pi.arm3   (0-255)

# a = random.randint(1, 3) # Arm
# b = random.randint(1, 6) # Colour
# c = random.randint(1, 18) # LED
# d = random.randint(0, 255) # Brightness

while True:
    pi = PiGlow()
    n = int(input('Enter a number: '))
    for x in range(1, n):
        b = random.randint(1, 6)
        d = random.randint(0, 255)
        pi.colour(b, d)
        t = random.uniform(0.05, 0.1)
        time.sleep(t)
        pi.all(0)

import math
import random

#Dimming LED
for ii in range(0,25):
    print('')

#"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
from analogio import AnalogIn

analog_in_g = AnalogIn(board.GP26)
analog_in_r = AnalogIn(board.GP27)
analog_in_b = AnalogIn(board.GP28)

led_g = pwmio.PWMOut(board.GP14, frequency=1000, duty_cycle=int(65535))
led_r = pwmio.PWMOut(board.GP15, frequency=1000, duty_cycle=int(65535))
led_b = pwmio.PWMOut(board.GP13, frequency=1000, duty_cycle=int(65535))




# = 0

while True:
    #time.sleep(0.1)
    g = random.randint(0,65534)
    print(g)
    b = random.randint(0,65534)
    print(b)
    r = random.randint(0,65534)
    print(r)
    #led_g = pwmio.PWMOut(board.GP14, frequency=1000, duty_cycle=int(65535))
    #led_r = pwmio.PWMOut(board.GP15, frequency=1000, duty_cycle=int(65535))
    #led_b = pwmio.PWMOut(board.GP13, frequency=1000, duty_cycle=int(65535))
    led_g.duty_cycle = int(g)
    led_r.duty_cycle = int(r)
    led_b.duty_cycle = int(b)
    time.sleep(1)
   #i=i+1

print('done')

#Gamma Correction

# Write your code here :-)

import math

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

led_g = pwmio.PWMOut(board.GP14, frequency=1000, duty_cycle=int(65535/8))
led_r = pwmio.PWMOut(board.GP15, frequency=1000, duty_cycle=int(65535/8))
led_b = pwmio.PWMOut(board.GP13, frequency=1000, duty_cycle=int(65535/8))

while True:
    time.sleep(0.1)
    led_g.duty_cycle = analog_in_g.value
    led_r.duty_cycle = analog_in_r.value
    led_b.duty_cycle = analog_in_b.value

print('done')

#Gamma Correction

# Write your code here :-)

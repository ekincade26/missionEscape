# Write your code here :-)
import board
import time
#pwmio module contains classes to provide access to basic pulse IO
import pwmio
#to let us read in from blue knob
from analogio import AnalogInputDevice

#read in and save value from blue knob
analog_in = AnalogIn(board.GP26)

#LED
led = pwmio.PWMOut(board.GP15, frequency = 1000, duty_cycle=int(65535/8))

while True:
    time.sleep(0.1)
    led.duty_cycle = analog_in.value

print('\n\nEnd of line')

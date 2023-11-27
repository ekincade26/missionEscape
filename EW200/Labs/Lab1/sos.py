# importing libraries
import board

# importing only DigitalInOut and Direction from the digital library
from digitalio import DigitalInOut, Direction

# time based library
import time

# r_led on the breadboard
# LED connected to port GP15 of Pico
# set as output because we are sending information to the LED
r_led = DigitalInOut(board.GP15)
r_led.direction = Direction.OUTPUT

# poor man's clear screen
for ii in range(0,25):
    print(' ')

# set the output to the value.
#r_led.value = True
#time.sleep(3)

#r_led.value = False
#time.sleep(2)
#print('next action')
# print SOS
print('SOS')

j = 0
while j < 3:
    r_led.value = True
    time.sleep(.25)
    print('On')
    r_led.value = False
    time.sleep(.25)
    print('Off')
    j = j+1

i = 0
while i < 3:
    r_led.value = True
    time.sleep(1)
    print('On')
    r_led.value = False
    time.sleep(1)
    print('Off')
    i = i+1

k = 0
while k < 3:
    r_led.value = True
    time.sleep(.25)
    print('On')
    r_led.value = False
    time.sleep(.25)
    print('Off')
    k = k+1

# to make sure it ran
print('\n\nEnd of line.')# Write your code here :-)

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

i = 0
while i < 4:
    if i == 0:
        j = .1
        k = .1
        print('Faster Blink')
    elif i == 1:
        j = .01
        k = .01
        print('Fast Blink: Balanced')
    elif i == 2:
        j = .019
        k = .001
        print('Fast Blink: Mostly ON')
    elif i == 3:
        j = .001
        k = .019
        print('Fast Blink: Mostly OFF')
    r_led.value = True
    time.sleep(j)
    print('On')
    r_led.value = False
    time.sleep(k)
    print('Off')
    #because it's flashing too fast and I can't see it
    time.sleep(1)
    i = i+1

print('Fast Blink: Mostly ON')



# to make sure it ran
print('\n\nEnd of line.')# Write your code here :-)

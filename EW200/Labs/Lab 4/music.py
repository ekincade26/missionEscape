import time
import board
import pwmio
from analogio import AnalogIn


music = pwmio.PWMOut(board.GP1, frequency = 1000, duty_cycle=int(65535/2),variable_frequency=True)
G = 391.995
D = 293.665
E = 329.628
A = 440
B = 493.880
R = 0
song = [G,G,G,D,E,E,D,B,B,A,A,G,R,D,G,G,G,D,E,E,D,B,B,A,A,G,R,D,D,G,G,G,D,D,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,D,E,E,D,B,B,A,A,G,R]


while False:
    for note in song:
        if note == R:
            music.duty_cycle = 0
            time.sleep(.25)
        else:
            music.frequency= int(note)
            print(note)
            time.sleep(.25)
            music.duty_cycle = 0
            time.sleep(.25)
            music.duty_cycle=int(65535/2)# Write your code here :-)

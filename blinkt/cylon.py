# cylon.py
# produce pulsing light sequence inspired by Battlestar Galactica

# import modules
import blinkt
from time import sleep

# define variables
pattern = [[0,0,0,1,1,0,0,0],
           [0,0,1,1,1,1,0,0],
           [0,1,1,0,0,1,1,0],
           [1,1,0,0,0,0,1,1],
           [1,0,0,0,0,0,0,1],
           [0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,1],
           [1,1,0,0,0,0,1,1],
           [0,1,1,0,0,1,1,0],
           [0,0,1,1,1,1,0,0],
           [0,0,0,1,1,0,0,0],
           [0,0,0,0,0,0,0,0]]

# set brightness
blinkt.set_brightness(0.1)

# main loop - run indefinitely
try:
    while True:
        for lines in pattern:
            for i in range(8):
                if lines[i] == 1:
                    blinkt.set_pixel(i, 255, 0, 0)  # turn pixel red
                else:
                    blinkt.set_pixel(i, 0, 0, 0)
            blinkt.show()
            sleep(0.1)

except:
    # clean up if ctrl-c is pressed. Turn all pixels off
    for i in range(8):
        blinkt.set_pixel(i, 0, 0, 0)

    blinkt.show()

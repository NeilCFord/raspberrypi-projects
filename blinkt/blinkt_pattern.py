# blinkt_pattern.py
# produce pulsing light sequence read from a file.
# an improvement on cylon.py

# import modules
import blinkt, sys, os
from time import sleep

# set brightness
blinkt.set_brightness(0.1)


# read in file
filename = sys.argv[1]+".csv"
if os.path.isfile(filename):
    # file exists, read file and create pattern list
    fh = open(filename, "r")
    records = fh.readlines()
    pattern = []
    for record in records:
        record = record.strip()
        a, b, c, d, e, f, g, h = record.split(',')
        pattern.append([a, b, c, d, e, f, g, h])
else:
    print("Sorry, " + filename + " not found!")
    exit()
        
# main loop - run indefinitely
try:
    while True:
        for lines in pattern:
            for i in range(8):
                if lines[i] == "1":
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

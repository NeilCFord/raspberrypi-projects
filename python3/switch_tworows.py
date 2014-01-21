#!/usr/bin/python3

# import modules
import RPi.GPIO as GPIO
from time import sleep
import random
  
# set variables
red1 = 17
green1 = 22
yellow1 = 10
red2 = 9
green2 = 14
yellow2 = 15
switch_pin = 23

# set-up GPIO states
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(yellow1, GPIO.OUT)
GPIO.setup(green1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

# main loop
while True:

    print("Press the Switch!")
        
    if (GPIO.input(switch_pin) == False):
        print("Switch Pressed\n")

        # turn off all leds
        GPIO.output(red1, False)
        GPIO.output(yellow1, False)
        GPIO.output(green1, False)
        GPIO.output(red2, False)
        GPIO.output(yellow2, False)
        GPIO.output(green2, False)

        times = random.randint(3, 7)
        print("time is ", times)

        for n in range(times):

            # turn on red leds
            GPIO.output(red1, True)
            GPIO.output(red2, True)
            print ("red in ON")
            sleep(1)
            GPIO.output(red1, False)
            GPIO.output(red2, False)

            # turn on yellow leds
            GPIO.output(yellow1, True)
            GPIO.output(yellow2, True)
            print("yellow is ON")
            sleep(1)
            GPIO.output(yellow1, False)
            GPIO.output(yellow2, False)
        
            # turn on green leds
            GPIO.output(green1, True)
            GPIO.output(green2, True)
            print("green is ON")
            sleep(1)
            GPIO.output(green1, False)
            GPIO.output(green2, False)


        print("End\n")

    sleep(0.5)
    


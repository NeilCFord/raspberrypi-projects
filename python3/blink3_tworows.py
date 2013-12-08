#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

# set variables
red1 = 17
green1 = 22
yellow1 = 10
red2 = 9
green2 = 14
yellow2 = 15

# setup gpio mode and pins
print ("Setting up GPIO")

GPIO.setmode(GPIO.BCM)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(yellow1, GPIO.OUT)
GPIO.setup(green1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)

# light the LEDs 5 times
for n in range(5):

        # turn off all leds
        GPIO.output(red1, False)
        GPIO.output(yellow1, False)
        GPIO.output(green1, False)
        GPIO.output(red2, False)
        GPIO.output(yellow2, False)
        GPIO.output(green2, False)

        # turn on red leds
        GPIO.output(red1, True)
        GPIO.output(red2, True)
        print ("red in ON")
        sleep(2)
        GPIO.output(red1, False)
        GPIO.output(red2, False)

        # turn on yellow leds
        GPIO.output(yellow1, True)
        GPIO.output(yellow2, True)
        print("yellow is ON")
        sleep(2)
        GPIO.output(yellow1, False)
        GPIO.output(yellow2, False)
        
        # turn on green leds
        GPIO.output(green1, True)
        GPIO.output(green2, True)
        print("green is ON")
        sleep(2)
        GPIO.output(green1, False)
        GPIO.output(green2, False)


# turn off all leds
GPIO.output(red1, False)
GPIO.output(yellow1, False)
GPIO.output(green1, False)
GPIO.output(red2, False)
GPIO.output(yellow2, False)
GPIO.output(green2, False)

# clean up gpio
print("End")
GPIO.cleanup()

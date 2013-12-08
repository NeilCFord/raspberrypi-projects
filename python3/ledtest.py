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

GPIO.setmode(GPIO.BCM)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(yellow1, GPIO.OUT)
GPIO.setup(green1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)

GPIO.output(red1, False)
GPIO.output(yellow1, False)
GPIO.output(green1, False)
GPIO.output(red2, False)
GPIO.output(yellow2, False)
GPIO.output(green2, False)

print("red")
GPIO.output(red2, True)
sleep(2)
GPIO.output(red2, False)

print("yellow")
GPIO.output(yellow2, True)
sleep(2)
GPIO.output(yellow2, False)

print("green")
GPIO.output(green2, True)
sleep(2)
GPIO.output(green2, False)

GPIO.output(red1, False)
GPIO.output(yellow1, False)
GPIO.output(green1, False)
GPIO.output(red2, False)
GPIO.output(yellow2, False)
GPIO.output(green2, False)

GPIO.cleanup()

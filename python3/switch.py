#!/usr/bin/python3

# import modules
import RPi.GPIO as GPIO
from time import sleep
import random
  
# set-up variables
red = 17
green = 22
yellow = 10
led_pin = red
switch_pin = 23

# set-up GPIO states
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

# enable_led function
def enable_led(should_enable):
	if should_enable:
		GPIO.output(led_pin, True)
	else:
		GPIO.output(led_pin, False)

# main loop
while True:

    print("Press the Switch!")
        
    if (GPIO.input(switch_pin) == False):
        print("Switch Pressed\n")

        times = random.randint(3, 7)
        print("time is ", times)

        for n in range(times):
            enable_led(False)
            led_pin = red
            enable_led(True)
            print ("red in ON")
            sleep(2)
        
            enable_led(False)
            led_pin = yellow
            enable_led(True)
            print("yellow is ON")
            sleep(2)

            enable_led(False)
            led_pin = green
            enable_led(True)
            print("green is ON")
            sleep(2)


        enable_led(False)
        print("End\n")

    sleep(0.5)
    


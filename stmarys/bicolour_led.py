
import RPi.GPIO as GPIO
import time
# Set the numbering sequence of the pins, then set pins ten and twelve to output, and pin eight to input.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(8, GPIO.IN)
# Turn both of the LEDs off.
GPIO.output(10, True)
GPIO.output(12, True)
# The SwitchState variable is 1 if the button is pressed, and 0 otherwise. LEDState is 0 when off, 1 when red, and 2 when green.
SwitchState = 0
LEDState = 0

while 1:
    if GPIO.input(8)
# When the LED is off, keep the green LED off, turn the red one on, then change the state of the LED to reflect that it is red, and wait one second.
        if LEDState == 0
            GPIO.output(10, True)
            GPIO.output(12, False)
            LEDState = 1
            time.sleep(1)

# When the LED is red, turn the green LED on, turn the red one off, then change the state of the LED to reflect that it is green, and wait one second.
        elif LEDState == 1
            GPIO.output(10, False)
            GPIO.output(12, True)
            LEDState = 2
            time.sleep(1)

# When the LED is green, turn it off, then turn the red one off, then change the state of the LED to reflect that they are all off, and wait one second.
        elif LEDState == 2
            GPIO.output(10, True)
            GPIO.output(12, True)
            LEDState = 0
            time.sleep(1)
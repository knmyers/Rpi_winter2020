# 06_reactions.py
# Adapted from the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time, random

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
# pins used for the LED and switches
        
red_pin = 17
green_pin = 27
red_switch = 22
green_switch = 10

# LED pins outputs, switch inputs


class ReactionTime:
    def __init__(self,output_pin1, output_pin2, input_pin1, input_pin2):
        self.red_pin = output_pin1
        self.green_pin = output_pin2
        self.red_switch = input_pin1
        self.green_switch = input_pin2


    def _on(self, pin):
        GPIO.output(pin, True)

    def _off(self, pin):
        GPIO.output(pin, False)

    # The next three functions turn appropriate LEDs on and off
    def green(self):
        self._on(self.green_pin)
        self._off(self.red_pin)

    def red(self):
        self._on(self.red_pin)
        self._off(self.green_pin)

    def off(self):
        self._off(self.red_pin)
        self._off (self.green_pin)

# find which buttons pressed -1 means neither, 0=both, 1=red, 2=green 
def key_pressed(self):
    red = GPIO.input(self.red_switch)
    green = GPIO.input(self.green_switch)

    if red:
        if green:
            return 0  # red and green
        else:
            return 1  # Only red
    elif green:
        return 2  # Only green
    else:
        return -1  # Nothing

try:        
    while True:
        off()
        print("Press the button for red or green when one lights")
        delay = random.randint(3, 7)    # random delay of 3 to 7 seconds
        color = random.randint(1, 2)    # random color red=1, green=2
        time.sleep(delay)
        if (color == 2):
            red()
        else:
            green()
        t1 = time.time()
        while not key_pressed():
            pass
        t2 = time.time()
        if key_pressed() == 0 : # if both buttons are pressed,Exit
            break
        elif key_pressed() != color :   # check the right buton was pressed
            print("WRONG BUTTON")
        else:
            # display the response time
            print("Time: " + str(int((t2 - t1) * 1000)) + " milliseconds")
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.
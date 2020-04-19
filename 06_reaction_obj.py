# 06_reactions.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

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
    def __init__(self,red_pin, green_pin, red_switch, green_switch):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.red_switch = red_switch
        self.green_switch = green_switch

    def setup(self, input, output, on):
        GPIO.setup(input, GPIO.IN)
        GPIO.setup(output, GPIO.OUT)
        GPIO.output(output,on)

    def on_off(self):
        self.on = input, true
        self.off = input, false



# The next three functions turn appropriate LEDs on and off
def green():
    GPIO.output(green_pin, True)
    GPIO.output(red_pin, False)

def red():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, True)

def off():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, False)

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
        if key_pressed() != color :   # check the right buton was pressed
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
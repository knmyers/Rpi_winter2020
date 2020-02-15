# 02_blink_twice.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)


class LED:
    state = False
    
    def _init_(self, start_state, id_pin):
        self.state =start_state
        self.pin = id_pin
        
red_LED1 = LED(True,14)
red_LED2 = LED (True,19)

GPIO.setmode(red_LED1,red_LED2,GPIO.OUT)

        
try:
    while True:
        GPIO.output(red_LED1, red_LED2,True)     # True means that LED turns on
        #GPIO.output(red_LED2, False)    # False means that LED turns off
        time.sleep(0.5)                 # delay 0.5 seconds
        red_LED1.state = not red_LED1.state
        red_LED2.state = not red_LED2.state
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.

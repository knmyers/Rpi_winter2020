# 01_blink.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com


import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)






class LED:
    state = False
    def __init__(self,start_state,id_pin):
        self.state = start_state
        self.pin = id_pin
        
red_LED = LED(True,14)

GPIO.setup(red_LED.pin, GPIO.OUT)

try:         
    while True:
        GPIO.output(red_LED.pin,red_LED.state)  # LED on
        time.sleep(0.5)# delay 0.5 seconds
        red_LED.state = not red_LED.state   
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
# You could get rid of the try: finally: code and just have the while loop
# and its contents. However, the try: finally: construct makes sure that
# when you CTRL-c the program to end it, all the pins are set back to 
# being inputs. This helps protect your Pi from accidental shorts-circuits
# if something metal touches the GPIO pins.
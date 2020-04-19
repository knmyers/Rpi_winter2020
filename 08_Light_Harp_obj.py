# 08_light_harp.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time, math
from thermometer_plus_obj import ThermometerPlus

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 
a_pin = 17
b_pin = 27
buzzer_pin = 22

GPIO.setup(buzzer_pin, GPIO.OUT)
class LightHarp(ThermometerPlus):
    def __init__(self, a_pin, b_pin, buzzer):
        super().__init__(a_pin, b_pin, buzzer)




# Rather misleadingly, this function actually makes the tone on the buzzer
# by turning it on and off, with a delay caused by charge_time.
# Cunning or what?
    def analog_read(self):
        self.discharge()
        GPIO.output(self.buzzer, True)
        self.discharge()
        self.charge_time()
        GPIO.output(self.buzzer, False)
        self.charge_time()

try:
    while True:
        analog_read()

finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.
# 07_light_meter.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from tkinter import *
import RPi.GPIO as GPIO
import time, math
from Thermometer import Thermometer

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# This project uses a photoresistor, a component whose resistance varies with the light falling on it.
# To measure its resistance, the code records the time it takes for a capacitor to fill  
# when supplied by a current passing through the resistor. The lower the resistance the faster 
# it fills up. 
#
# You can think of a capacitor as a tank of electricity, and as it fills with charge, the voltage
# across it increases. We cannot measure that voltage directly, because the Raspberry Pi
# does not have an analog to digital convertor (ADC or analog input). However, we can time how long it
# takes for the capacitor to fill with charge to the extent that it gets above the 1.65V or so
# that counts as being a high digital input. 
# 
# For more information on this technique take a look at: 
# learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi
# The code here is based on that in the Raspberry Pi Cookbook (Recipes 12.1 to 12.3)


# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 

class Lightmeter(Thermometer):
    def __init__(self, a_pin, b_pin):
        super().__init__(a_pin, b_pin)
# empty the capacitor ready to start filling it up


# Take an analog reading as the time taken to charge after first discharging the capacitor
    def analog_read(self):
        self.discharge()
        return self.charge_time()

# Convert the time taken to charge the capacitor into a value of resistance
# To reduce errors, do it 100 times and take the average.
    def read_resistance(self):
        n = 100
        total = 0
        for _ in range(n): # don't make veriables that aren't used
            total = total + self.analog_read()
        reading = total / float(n)
        resistance = reading * 6.05 - 939
        return resistance

    def light_from_r(self,R):
        # Log the reading to compress the range
        return math.log(1000000.0/R) * 10.0
light_meter =Lightmeter(17,27)
# group together all of the GUI code into a class called App
class App:
    
    # this function gets called when the app is created
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Light', font=("Helvetica", 32))

        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    # Update the reading
    def update_reading(self):
        light = light_meter.light_from_r(light_meter.read_resistance())
        reading_str = "{:.0f}".format(light)
        self.reading_label.configure(text=reading_str)
        self.master.after(200, self.update_reading)

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('Light Meter')
app = App(root)
root.geometry("400x300+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()


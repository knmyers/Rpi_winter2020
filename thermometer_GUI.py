# 04_thermomether.py
# adapted from the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from tkinter import *           # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time
import math

C = 0.38 # uF - Tweek this value around 0.33 to improve accuracy
R1 = 1000 # Ohms
B = 3800.0 # The thermistor constant - change this for a different thermistor
R0 = 1000.0 # The resistance of the thermistor at 25C -change for different thermistor


# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# This project uses a thermistor, a component whose resistance varies with the temperature.
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


therm = Thermometer(17, 27)
# group together all of the GUI code into a class called App
class App:

    # this function gets called when the app is created
    def __init__(self, master):
        self.master = master
        # A frame holds the various GUI controls
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Temp C', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    # Update the temperature reading
    def update_reading(self):
        temp_c = therm.read_temp_c()
        reading_str = "{:.2f}".format(temp_c)
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading) # schedule yourself to be called after 0.5 seconds

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('Thermometer')
app = App(root)
root.geometry("400x300+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()

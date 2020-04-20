# 05_thermometer_plus.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from tkinter import *           # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time, math
from thermometer_GUI import Thermometer


C = 0.38 # uF - Tweek this value around 0.33 to improve accuracy
R1 = 1000 # Ohms
B = 3800.0 # The thermistor constant - change this for a different thermistor
R_0 = 1000.0 # The resistance of the thermistor at 25C -change for different thermistor
set_temp = 25           # The temperature above which the buzzer will sound

# The type of capacitors only have an accuracy of +-10% on its stated value and there are
# other components that will not be exactly the value stated on the package
# changing the fiddle_factor will help compensate for this.
# fiddle with the fiddle_factor (keep it close to 1.0) until this project agrees with a
# thermometer you trust.
# To be honest, its never going to be very accurate, as an absolute thermometer,
# but the value of temp should increase when you hold the thermistor between you fingers to
# warm it up.

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



class ThermometerPlus(Thermometer):
    def __init__(self, a_pin, b_pin, buzzer ):
        super().__init__(a_pin, b_pin)
        self.buzzer = buzzer
        GPIO.setup(buzzer, GPIO.OUT)

# sound the buzzer at a certain pitch (in Hz) for a duration in seconds
    def buzz(self, pitch, duration):
        period = 1.0 / pitch            # period of cycle
        delay = period / 2              # delay half of period (2 delays per cycle)
        cycles = int(duration * pitch)  # total number of cycles needed for duration specified
        for _ in range(cycles):         # turn buzzer on and off for number of cycles needed
            GPIO.output(self.buzzer, True)
            time.sleep(delay)
            GPIO.output(self.buzzer, False)
            time.sleep(delay)
therm_plus = ThermometerPlus(17,27,22)
# group together all of the GUI code into a class called App
class App:

    # this function gets called when the app is created
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Temp C', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    # Update the temperature reading
    def update_reading(self):
        temp_c = therm_plus.read_temp_c()
        if temp_c > set_temp:
            therm_plus.buzz(500, 0.3)
        reading_str = "{:.2f}".format(temp_c)
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading)

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

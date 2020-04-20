from tkinter import *           # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time
import math



GPIO.setmode(GPIO.BCM)

class Thermometer:
    def __init__(self, a_pin, b_pin):
        self.a_pin = a_pin
        self.b_pin = b_pin

    def setup(self, input, out, on):
        GPIO.setup(input, GPIO.IN)
        GPIO.setup(out, GPIO.OUT)
        GPIO.output(out, on)
    # find something realtively close to the ambient temp
# empty the capacitor ready to start filling it up
    def discharge(self):
        self.setup(self.a_pin, self.b_pin, False)
        time.sleep(0.01)

# return the time taken for the voltage on the capacitor to count as a digital input HIGH
# than means around 1.65V
    def charge_time(self):
        self.setup(self.b_pin, self.a_pin, True)
        t1 = time.time()
        while not GPIO.input(self.b_pin):
         pass
        t2 = time.time()
        return (t2 - t1) * 1000000 # microseconds

# Take an analog reading as the time taken to charge after first discharging the capacitor
    def analog_read(self):
        self.discharge()
        t = self.charge_time()
        self.discharge()
        return t

# Convert the time taken to charge the cpacitor into a value of resistance
# To reduce errors, do it lots of times and take the average.
    def read_resistance(self):
        n = 10
        total = 0;
        for i in range(0, n):
            total = total + self.analog_read()
        t = total / float(n)
        T = t * 0.632 * 3.3
        r = (T / C) - R1
        return r


    def read_temp_c(self):
        R = self.read_resistance()
        t0 = 273.15     # 0 deg C in K
        t25 = t0 + 25.0 # 25 deg C in K
    # Steinhart-Hart equation - Google it
        inv_T = 1/t25 + 1/B * math.log(R/float(R0))
        T = (1/inv_T - t0)
        return T

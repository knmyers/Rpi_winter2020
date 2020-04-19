#03_rgb.py
# adapted From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com
# Based on Recipe 9.9 in The Raspberry Pi Cookbook by Simon Monk.

from tkinter import *       # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
"used a 'super' class to give my PWM class the same functions as the parent GPIO.PWM class)
class PWM(GPIO.PWM):
    def __init__(self, id_pin, start_state, maximum, color):
        GPIO.setup(id_pin, GPIO.OUT)
        self.pwm = super().__init__(id_pin, maximum)
        super().start(start_state)
        self.color = color
        
    def update(self,duty):
        super().ChangeDutyCycle(float(duty))
Red = PWM(17,100,500,"Red")
Green = PWM(27,100,500,"Green")
Blue = PWM(22,100,500,"Blue")
LEDs = [Red, Green, Blue]
# Start Pulse Width Modulation (PWM) on the red, green and blue channels to 
# control the brightness of the LEDs.
# Follow this link for more info on PWM: http://en.wikipedia.org/wiki/Pulse-width_modulation
# pwmRed = GPIO.PWM(17, 500)
# pwmRed.start(100)

# pwmGreen = GPIO.PWM(27, 500)
# pwmGreen.start(100)

# pwmBlue = GPIO.PWM(22, 500)
# pwmBlue.start(100)


# group together all of the GUI code into a class called App
class App:
    
    # this function gets called when the app is created
    def __init__(self, master):
        # A frame holds the various GUI controls
        frame = Frame(master)
        frame.pack()
        
        for i, led in enumerate(LEDs):
            
            # Create the labels and position them in a grid layout
            Label(frame, text=led.color).grid(row=i, column=0)
            scale = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=led.update)
            scale.grid(row=i,column=1)

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('RGB LED Control')
app = App(root)
root.geometry("200x150+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()


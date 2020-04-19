# 10_email_notifier.py
# adapted from the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com
# Based on Recipe 7.15 in The Raspberry Pi Cookbook by Simon Monk.

import RPi.GPIO as GPIO
import smtplib, time            # smtp - Simple Mail Transport Protocol - library for sending email

SMTP_SERVER = 'smtp.gmail.com'
"TLS"
SMTP_PORT = 587

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
#chose a blue LED because it makes me less anxious, you can change it to red
GPIO.setmode(GPIO.BCM)
blue_pin = 17
green_pin = 27
switch_pin = 22

GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Use the smtp library to send an email 
def send_email(username, password, recipient, subject, text):
    print(username, password, recipient, subject, text)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    header = 'To:' + recipient + '\n' + 'From: ' + username
    header = header + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(username, recipient, msg)
    smtpserver.close()

# Utility function to turn the green LED on and the blue off
#def green():
    #GPIO.output(green_pin, True)
    #GPIO.output(blue_pin, False)

# Utility function to turn the blue LED on and the green off
#def red():
    #GPIO.output(green_pin, False)
    #GPIO.output(blue_pin, True)

#implemented the LED class from bink to control my LED pins"   
class LED:
     #state = False
    
    def __init__(self, start_state, id_pin):
        self.state = start_state
        self.pin = id_pin
        GPIO.setup(self.pin, GPIO.OUT)
    
    def switch(self):
        self.state = not self.state
        GPIO.output(self.pin, self.state)
            
  #setting pins on the board      
blue_LED = LED(False,17)
green_LED = LED(False,22)

#rewrote the utility function using my LED class
def green():
        blue_LED.switch()
def blue():
        green_LED.switch()
# Prompt the user to enter their email details
# Should only have to do this once each time the program is started
#had to update the code from python 2 to python3
username = input("Sending gmail address? ")
password = input("Sending gmail password? ")
recipient = input("Send email to? ")
subject = input("Subject? ")
message = input("Message ? ")

print("Press the button to send the Email")

while True:
    green()                                 # green LED on
    if GPIO.input(switch_pin) == False:     # button pressed - led red 
        red()
        send_email(username, password, recipient, subject, message)
        time.sleep(3)
        print("Press the button to send the Email")

#default pull down input to button high

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

#A GPIO event in the Raspberry Pi Python GPIO library works by calling a Python function whenever an event is triggered. 
#Such a function is called a callback function.
def button_callback(channel):
    print("Button was pushed!")
	

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (ground default input

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge(when button pushed=low to high=rise)

message = input("Press enter to quit\n\n") # Run forever, until someone presses enter
GPIO.cleanup() # Clean up



#execute: $ python3 push_button.py  
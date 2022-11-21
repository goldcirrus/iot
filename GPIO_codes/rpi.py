   import RPi.GPIO as GPIO   
                                      
   GPIO.setmode(GPIO.BCM)                 # for GPIO numbering, choose BCM    
                                       
   GPIO.setmode(GPIO.BOARD)               # or, for pin numbering, choose BOARD 
  
# but you can't have both, so only use one!!!  

   GPIO.setup(Port_or_pin, GPIO.IN)       #to set up a GPIO port as an input. 
                                          #…changing Port_or_pin to the number of the GPIO port or pin you want to use.                                        
   GPIO.setup(25, GPIO.IN)                #I’m going to use the BCM GPIO numbering and port GPIO25, so it becomes

#set input pin (high/1 or ground/0)
import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input  

#input with a default pulldown and button to 3.3V High.(input is grounded default when button not pushed). (When button pushed, input receive high). 
#inputs are Boolean values: 1 or 0, GPIO.HIGH or GPIO.LOW, True or False (this corresponds to the voltage on the port: 0V=0 or 3.3V=1).
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(25): # if port 25 == 1, 3.3V high voltage linked to input
            print "Port 25 is 1/GPIO.HIGH/True - button pressed"  
        else:  
            print "Port 25 is 0/GPIO.LOW/False - button not pressed(default ground input)"  
        sleep(0.1)         # wait 0.1 seconds  
	
button_press = GPIO.input(25)                # or store its value in a variable

except KeyboardInterrupt:  
    GPIO.cleanup()         # clean up after yourself  
	
#enable these internal pull-ups/pull-downs at the time of setting up the port for input or output, by adding an extra, optional, argument to the GPIO.setup() function call.
GPIO.setup(port_or_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    #can change the PUD_DOWN for PUD_UP
#old with external pull-ups/pull-downs circuit wiring
GPIO.setup(25, GPIO.IN) # set GPIO25 as input (button)
#new with internal pull-ups/pull-downs
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set GPIO25 as input (button)


##############################
GPIO.setup(port_or_pin, GPIO.OUT)   #Setting up port/pin for output
GPIO.setup(port_or_pin, GPIO.OUT, initial=1)    #also set the initial value of the output at the time of setting up the port
GPIO.setup(port_or_pin, GPIO.OUT, initial=0)
GPIO.output(port_or_pin, 1)         #to switch the port/pin to 3.3V (equals 1/GPIO.HIGH/True)…
GPIO.output(port_or_pin, 0)         #to switch the port/pin to 0V (equals 0/GPIO.LOW/False)…




#A working example. We’ll set up RPi.GPIO in BCM mode, set GPIO24 as an output, and switch it on and off every half second until we CTRL+C exit.
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   
  
try:  
    while True:  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # clean up GPIO on CTRL+C exit   
GPIO.cleanup()                     # clean up GPIO on normal exit 
	
	
	
	
	
#to read the status of an output pin. when using a port as an output, it might be useful to be able to “read” its status – whether it’s 1/GPIO.HIGH/True or 0/GPIO.LOW/False.
#can do this by treating it as an input port: GPIO.input(port_or_pin)
import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output 

try:
    while True:
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True to switch LED on
        sleep(0.5)                 # wait half a second
        if GPIO.input(24):             #treating GPIO24 as an input port
            print "LED just about to switch off"
        GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False to switch LED off.
        sleep(0.5)                 # wait half a second
        if not GPIO.input(24):          #treating GPIO24 as an input port
            print "LED just about to switch on"
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program

##########################combined
import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 15)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input (button)
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)

try:
    while True:            # this will carry on until you hit CTRL+C
        if GPIO.input(25): # if port 25 == 1(input recieve high when Button pushed)
            print "Port 25 input receive 1/HIGH/True - LED ON"
            GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True to turn on LED
        else:               # if port 25 == 0(input grounded as default wired and when Button is NOT pushed)
            print "Port 25 input receive 0/LOW/False - LED OFF"
            GPIO.output(24, 0)         # set port/pin value to 0/LOW/False to turn off LED
        sleep(0.1)         # wait 0.1 seconds

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself


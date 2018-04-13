from ky040 import KY040
import RPi.GPIO as GPIO
from time import sleep
from sous_videdb import SousVideDB

# How many degrees to vary the temp
increment = 5
#Low and high temperatures in farenheight
low_set = 50
high_set = 200

def main(): 
    GPIO.setmode(GPIO.BCM)
    # Define your pins
    CLOCKPIN = 22
    DATAPIN = 5
    SWITCHPIN = 6

    db = SousVideDB()
    
    # Callback for rotary change
    def rotaryChange(direction):
        print("direction =", direction)
        current = db.set_point[1] 
        print ('current setpoint - ', current) 
        if direction == 0 and current < high_set: 
            current += increment
            db.set_point = current
        elif direction == 1 and current > low_set: 
            current -= increment
            db.set_point = current
        print ("New setpoint - " + str(current))

    # Callback for switch button pressed
    def switchPressed():
        print ("button pressed")

    # Create a KY040 and start it
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)
    ky040.start()

    # Keep your proccess running
    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()
        GPIO.cleanup()

if __name__ == '__main__': 
    main()

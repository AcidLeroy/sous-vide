#!/usr/bin/env python3

from ky040 import KY040
import RPi.GPIO as GPIO
from time import sleep
from sous_videdb import SousVideDB
import json

# How many degrees to vary the temp
increment = 5
#Low and high temperatures in farenheight
low_set = 50
high_set = 200

def main(db): 
    GPIO.setmode(GPIO.BCM)
    config = json.load(open('config.json')) 
    # Define your pins
    CLOCKPIN = config['Rotary']['CLOCKPIN']
    DATAPIN = config['Rotary']['DATAPIN']
    SWITCHPIN = config['Rotary']['SWITCHPIN']
    # Intially set mode to automatic
    if db.mode == None: 
        db.mode = 'auto'
    # Initially set the setpoint to 100 if not already set
    sp = db.set_point
    if sp == None: 
        db.set_point = 100
    possible_modes = ['auto', 'manual']
    
    # Callback for rotary change
    def rotaryChange(direction):
        def auto_mode(): 
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
        
        def manual_mode(): 
            if direction == 0 : 
                print('Turning the relay on') 
                db.relay_on = True
            elif direction == 1 : 
                print('Turning the relay off') 
                db.relay_on = False
        states = {'auto': auto_mode, 'manual': manual_mode} 
        mode = db.mode[1]
        states[mode]()


    # Callback for switch button pressed
    def switchPressed():
        current_mode = db.mode[1]
        print('switch preseed!')
        if current_mode == 'auto': 
            print('changing mode to manual!') 
            db.mode = 'manual'
        elif current_mode == 'manual': 
            print('Changing mode to auto!')
            db.mode = 'auto'
        else : 
            db.mode = 'auto'
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
    with SousVideDB() as db: 
        main(db)

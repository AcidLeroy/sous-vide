#!/usr/bin/env python3

import RPi.GPIO as GPIO
from sous_videdb import SousVideDB
import time
import json

class Relay(object): 
    state = {True: GPIO.HIGH, False: GPIO.LOW} 

    def __init__(self, db, pin=26): 
        print('Using pin {} for relay'.format(pin))
        self.pin = pin 
        self.db = db
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        # Initially set the relay to be off
        self.db.relay_on = False

    def update(self): 
        """
        Read what the desired state is set to in the db and then write it to the device
        """
        val = self.db.relay_on[1]
        GPIO.output(self.pin, Relay.state[val]) 
        print('Setting relay on to: ', val)


def main(): 
    config = json.load(open('config.json'))
    with SousVideDB() as db:
        pin = config['Relay']['CTRL'] 
        r = Relay(pin=pin, db=db)
        while True: 
            r.update()
            time.sleep(1.0)


if __name__ == '__main__': 
    main()

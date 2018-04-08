import RPi.GPIO as GPIO
from sous_videdb import SousVideDB
import time

class Relay(object): 
    state = {True: GPIO.HIGH, False: GPIO.LOW} 
    def __init__(self, db, pin=26): 
        self.pin = pin 
        self.db = db
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
    def read_and_update(self): 
        """
        Read what the desired state is set to in the db and then write it to the device
        """
        val = self.db.relay_on[1]
        GPIO.output(self.pin, Relay.state[val]) 
        print('Setting relay on to: ', val)


def main(): 
    db = SousVideDB()
    r = Relay(pin=26, db=db)
    while True: 
        r.read_and_update()
        time.sleep(.1)


if __name__ == '__main__': 
    main()

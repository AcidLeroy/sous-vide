#!/usr/bin/env python3
import os
import glob
import time
from sous_videdb import SousVideDB
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

class Temperature(object): 
    def __init__(self, db, base_dir='/sys/bus/w1/devices/'): 
        self.device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.db = db
    def read_temp_raw(self): 
        with open(self.device_file, 'r') as f: 
            lines = f.readlines()
        return lines

    def update(self): 
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            # Update the database with the current temperature
            print('Current temp (F) = ', temp_f)
            self.db.current_temperature = temp_f
def main(): 
    with SousVideDB() as db: 
        t = Temperature(db=db)
        while True: 
            t.update()
            time.sleep(1)


if __name__ == '__main__': 
    main()

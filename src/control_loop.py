from sous_videdb import SousVideDB
import time

def manual_mode(db): 
    # Nothing needs to be done in manual mode. 
    # Somone may be setting the relays on and off else where. 
    print('manual mode')
    pass

def automatic_mode(db): 
    # In automatic mode we are going to be reading and writing to and from the 
    # sensors based on the set point
    print('automatic mode') 
    set_point = db.set_point[1]
    current_temp = db.current_temperature[1]
    print('set_point = ', set_point, ', current_temp = ', current_temp)
    if current_temp < set_point: 
        print('Turning relay on ')
        db.relay_on = True
    else: 
        print('Turning relay of ')
        db.relay_on = False

states = {'manual': manual_mode, 
        'auto': automatic_mode} 

def control_loop(db): 
    while True: 
        mode = db.mode[1]
        # Execute the mode
        states[mode](db) 
        time.sleep(1)


def main():
    with SousVideDB() as db: 
        control_loop(db)


if __name__ == '__main__':
    main()

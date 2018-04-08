from sous_videdb import SousVideDB

def test_getters_setters(): 
    # Notice that I need to grab the second value in the tuple. 
    # The first value is always the data!
    a = SousVideDB()
    a.set_point = 12
    assert a.set_point[1] == 12
    a.current_temperature = 66.6
    a.current_temperature[1] == 66.6
    a.mode = 'auto'
    assert a.mode[1] == 'auto'
    a.mode = 'manual'
    assert a.mode[1] == 'manual'
    a.relay_on = True
    assert a.relay_on[1] == True

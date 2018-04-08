from mock_control import MockControl
import numpy as np
import matplotlib.pyplot as plt

class MockSousVideController(object):
    def __init__(self):
        a = np.arange(0, 2*math.pi, .001)
        self.vals = np.sin(a)
        pass

    @property
    def temperature(self):
        pass
    @temperature.getter(self):
    def temperature()

def main():


if __name__ == '__main__':
    main()

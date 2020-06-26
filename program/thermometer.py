from datetime import datetime
import os
import glob
import sys
import time


class Thermometer:
    def __init__(self):
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read_temp_raw(self):
        with open(self.device_file,'r') as infile:
            lines = infile.readlines()
        return lines

    def get_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_f 


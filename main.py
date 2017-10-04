import os
import glob
import time
from datetime import datetime

def read_device_file(device):
    with open(device, 'r') as f:
        lines = f.readlines()
        f.close()

    return lines


def read_temp(device):
    lines = read_device_file(device)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(.2)
        lines = read_device_file(device)

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_str = lines[1][equals_pos+2:]
        temp = float(temp_str) / 1000
    else:
        temp = 999
    return temp

def main():
    # Ininitialize sensor
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
        
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')
        
    for dev in device_folder:
        print('%s,%s,%s' % (dev[dev.find('28-'):], read_temp(dev+'/w1_slave'), datetime.now()))


if __name__ == "__main__":
    main()


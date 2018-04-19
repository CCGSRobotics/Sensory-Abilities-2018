from py_read_serial import *
import sys
import time
'''
Put all the sensor names in this list here, and plug them in accordingly.
Make sure they are plugged in correctly, otherwise your data will be wrong.
'''
sys.stdout.write("cls")

while 1:
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    for x in range(2):
        sensor = readPins()
        if sensor['num'] == 0:
            print('The CO2 Content of the surrounding environment is',sensor['value'],'ppm (parts per million)')
        if sensor['num'] == 1:
            temp = round((57*(sensor['value']-20))/100)
            print('The current temperature is',temp,'*C')
        sys.stdout.write("\033[K")
    time.sleep(0.5)
    

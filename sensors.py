from py_read_serial import *
'''
Put all the sensor names in this list here, and plug them in accordingly.
Make sure they are plugged in correctly, otherwise your data will be wrong.
'''
sensors = ['CO2 Sensor']

while 1:
    sensor = readPins()
    ''' This for loop, loops though all the sensors in the "sensors" list,
        ensuring all sensors print out values. '''
    for x in range(len(sensors)):
        ''' The if statement checks if the serial signals ID,
            the first letter of the string sent over,
            corresponds with the number the sensor is in the list. '''
        if int(sensor['num']) == x:
            if(sensor[num] == 0):
                print('The CO2 Content of the surrounding environment is',sensor['value'],'ppm (parts per million)')
            if(sensor[num] == 1):
                print('The current temperature is',temp,'*C')
            ''' A print statement to display the values, according to the sensor. '''
            print('The',str(sensors[x]),'signal is',sensor['value'])

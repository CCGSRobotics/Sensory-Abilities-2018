from py_read_serial import *
'''
Put all the sensor names in this list here, and plug them in accordingly.
Make sure they are plugged in correctly, otherwise your data will be wrong.
'''
sensors = ['RED']

while 1:
    sensor = readPins()
    ''' This for loop loops though all the sensors in the "sensors" list,
        ensuring all sensors print out values. '''
    for x in range(len(sensors)):
        ''' The if statement checks if the serial signals ID,
            the first letter of the string sent over,
            corresponds with the number the sensor is in the list. '''
        if int(sensor['num']) == x:
            ''' A print statement to display the values, according to the sensor. '''
            print('The',str(sensors[x]),'signal is',sensor['value'])

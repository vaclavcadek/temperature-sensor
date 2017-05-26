import serial
from datetime import datetime

with open('temperatures.csv', 'a') as log:
    s = serial.Serial('/dev/ttyACM0', 9600)
    t = s.readline().strip()
    log.write('{timestamp},{temperature}\n'.format(timestamp=datetime.now(), temperature=t))

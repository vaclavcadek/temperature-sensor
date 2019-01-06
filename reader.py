import serial
from datetime import datetime

if __name__ == '__main__':
    with open('temperatures.csv', 'a') as log:
        try:
            s = serial.Serial('/dev/ttyACM0')
            s.flushInput()
            ser_bytes = s.readline()
            t = ser_bytes.decode('utf-8')
            log.write('{timestamp},{temperature}\n'.format(timestamp=datetime.now(), temperature=t))
        except serial.SerialException:
            print('No Serial Port Available!')

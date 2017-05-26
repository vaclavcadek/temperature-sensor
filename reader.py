import sched
import time
import serial
from datetime import datetime

s = sched.scheduler(time.time, time.sleep)


def read_signal(sc):
    with open('/home/pi/temperatures.csv', 'a') as log:
        serial = serial.Serial('/dev/ttyACM0', 9600)
        log.write('{timestamp},{temperature}\n'.format(timestamp=datetime.now(), temperature=23.0))
    s.enter(1, 1, read_signal, (sc,))

s.enter(1, 1, read_signal, (s,))
s.run()

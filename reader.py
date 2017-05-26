import sched
import time
import serial
from datetime import datetime

scheduler = sched.scheduler(time.time, time.sleep)


def read_signal(sc):
    with open('/home/pi/temperatures.csv', 'a') as log:
        s = serial.Serial('/dev/ttyACM0', 9600)
	t = s,readline().trim()
        log.write('{timestamp},{temperature}\n'.format(timestamp=datetime.now(), temperature=t))
    scheduler.enter(1, 1, read_signal, (sc,))

scheduler.enter(1, 1, read_signal, (scheduler,))
scheduler.run()

import serial
import time

try:
    ser = serial.Serial('/dev/tty.usbmodem1421')
    with open('log.txt', 'w') as f:
        f.write('time,temperature\n')
        while True:
            val = ser.readline()
            val = val.decode('utf-8')
            time_val = time.strftime("%H:%M:%S")
            f.write(",".join([time_val,
                     val]) + '\n')
            f.flush()
except KeyboardInterrupt:
    ser.close()

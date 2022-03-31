# VELLEMAN EXAMPLE
Below example sourcecode to send data to Velleman LED-display from MacOS
Be aware that the usb-name namenclature in Linux might be different.

1. First install requisites
2. Subsequently build this Velleman wheel package (bf_velleman)
3. run sample .py on a system where Velleman display is connected via USB to your computer

## Preparation 

### Install dependencies sample program
pip3 install pyserial

### Build and install Velleman wheel for sample program
python3 setup.py bdist_wheel
pip3 install dist/bf_velleman-1.0.0-py2.py3-none-any.whl (our wheel dist)

### run sample program
python3 sample.py


## Example

### save example as sample.py

#!/usr/bin/python3
import os
import sys
import serial
import serial.tools.list_ports

from bf_velleman import *

def find_serial_port(filter):
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        usb_port = str(port)
        if filter in usb_port:
            return usb_port
    return None


def display_line(serial_connection, format, page):
    line = send_page(ID00, 1, page, COLOR_RED, WAIT_3S, format)
    print(line)
    time.sleep(1)
    serial_connection.write(line.encode())


def display_link(serial_connection, pages):
    line = link_pages(ID00, pages)
    print(line)
    time.sleep(1)
    serial_connection.write(line.encode())


if __name__ == "__main__":
    port = find_serial_port("cu.usb")
    if port is None:
        print('Failed: cannot find USB-port with a connected Velleman display')
        sys.exit(1)
    serial_connection = serial.Serial(port
                                      , baudrate='9600'
                                      , parity=serial.PARITY_NONE
                                      , stopbits=1
                                      , bytesize=serial.EIGHTBITS
                                      , xonxoff=True
                                      , rtscts=False
                                      , dsrdtr=False
                                      )
    if serial_conenction is None:
        print('Failed: cannot establish connection to Velleman display')
        sys.exit(1)

    display_line(serial_connection, 'Hello World!', 'A')
    display_line(serial_connection, 'It works', 'B')
    display_link(serial_connection, 'AB')
    serial_connection.close()
    sys.exit(0)

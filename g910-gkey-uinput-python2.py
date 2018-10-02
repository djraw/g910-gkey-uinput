#!/usr/bin/python

import uinput
import pyudev
import glob
import struct
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

context = pyudev.Context()

device = None
for hidraw in glob.glob("/dev/hidraw*"):
    dev = pyudev.Devices.from_device_file(context, hidraw)
    if "046D:C335.0004" in dev.device_path:
        device = hidraw

g1 = uinput.KEY_F17
g2 = uinput.KEY_F18
g3 = uinput.KEY_F20
g4 = uinput.KEY_F21
g5 = uinput.KEY_F22
g6 = uinput.KEY_F23
g7 = uinput.KEY_PROG1
g8 = uinput.KEY_PROG2
g9 = uinput.KEY_MSDOS
m1 = uinput.KEY_F13
m2 = uinput.KEY_F14
m3 = uinput.KEY_F15
mr = uinput.KEY_F16

f = open(device, 'rb')
device = uinput.Device((g1, g2, g3, g4, g5, g6, g7, g8, g9, m1, m2, m3, mr))

while True:
    binary = f.read(20)
    prefix = binary[0:3]
    binint = struct.unpack("b", binary[4])
    binint5 = struct.unpack("b", binary[5])

#debug lines
#    print int(binint[0]) & 2
#    print int(binint5[0]) & 1

    if prefix == b'\x11\xff\x08':
        device.emit(g1, int(binint[0]) & 1 != 0)
        device.emit(g2, int(binint[0]) & 2 != 0)
        device.emit(g3, int(binint[0]) & 4 != 0)
        device.emit(g4, int(binint[0]) & 8 != 0)
        device.emit(g5, int(binint[0]) & 16 != 0)
        device.emit(g6, int(binint[0]) & 32 != 0)
        device.emit(g7, int(binint[0]) & 64 != 0)
        device.emit(g8, int(binint[0]) & 128 != 0)
        device.emit(g9, int(binint5[0]) & 1 != 0)
    elif prefix == b'\x11\xff\t':
        device.emit(m3, int(binint[0]) & 1 != 0)
        device.emit(m2, int(binint[0]) & 2 != 0)
        device.emit(m1, int(binint[0]) & 4 != 0)
    elif prefix == b'\x11\xff\n':
        device.emit(mr, int(binint[0]) & 1 != 0)

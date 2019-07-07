# start the Bluetooth device
hciconfig hci0 up. 
# Scan the neighbour hood 
hcitool scan



#!/usr/bin/python 2 3 import lightblue 4 5 for device in lightblue.finddevices(): 6 print device[0] + " " + device[1] 
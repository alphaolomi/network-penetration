#!/usr/bin/python 
import getopt
import sys

import pcapy
from impacket.ImpactDecoder import EthDecoder

dev = "eth0"
filter = "arp"
decoder = EthDecoder()


# This function will be called for every packet 
# and just print it 

def handle_packet(hdr, data):
    print(decoder.decode(data))


def usage():
    print(sys.argv[0] + " -i <dev> -f <pcap_filter>")
    sys.exit(1)


# Parsing parameter 
try:
    cmd_opts = "f:i:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()

    for opt in opts:
        if opt[0] == "-f":
            filter = opt[1]
        elif opt[0] == "-i":
            dev = opt[1]
        else:
            # Open device in promisc mode
            pcap = pcapy.open_live(dev, 1500, 0, 100)
            # Set pcap filter
            pcap.setfilter(filter)
            # Start sniffing
            pcap.loop(0, handle_packet)

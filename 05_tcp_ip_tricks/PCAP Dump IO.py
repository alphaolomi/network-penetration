#!/usr/bin/python
import sys
from impacket.ImpactPacket import IP

dev = "eth0"
decoder = EthDecoder()
input_file = None
dump_file = "sniffer.pcap"


def write_packet(hdr, data):
    print(decoder.decode(data))
    dumper.dump(hdr, data)


def read_packet(hdr, data):
    ether = decoder.decode(data)
    if ether.get_ether_type() == IP.ethertype:
        iphdr = ether.child()
        tcphdr = iphdr.child()
        print(iphdr.get_ip_src() + ":" + str(tcphdr.get_th_sport()) + " -> " + iphdr.get_ip_dst() + ":" + str(
            tcphdr.get_th_dport()))


def usage():
    print(sys.argv[0] + """ 33 -i <dev> 34 -r <input_file> 35 -w <output_file>""")
    sys.exit(1)


# Parse parameter
try:
    cmd_opts = "i:r:w:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()
    for opt in opts:
        if opt[0] == "-w":
            dump_file = opt[1]
        elif opt[0] == "-i":
            dev = opt[1]
        elif opt[0] == "-r":
            input_file = opt[1]
        else:
            usage()

# Start sniffing and write packet to a pcap dump file
if input_file is None:
    pcap = pcapy.open_live(dev, 1500, 0, 100)
    dumper = pcap.dump_open(dump_file)
    pcap.loop(0, write_packet)

    # Read a pcap dump file and print it
else:
    pcap = pcapy.open_offline(input_file)
    pcap.loop(0, read_packet)
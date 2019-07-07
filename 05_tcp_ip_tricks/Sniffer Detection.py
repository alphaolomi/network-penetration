ifconfig -a | grep PROMISC 
cat /var/log/messages |grep promisc


1 #!/usr/bin/python 2 3 import sys 4 from scapy.all import promiscping 5 6 if len(sys.argv) < 2: 7 print sys.argv[0] + " <net>" 8 sys.exit() 9 10 promiscping(sys.argv[1]) 
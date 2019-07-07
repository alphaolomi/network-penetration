# SDP(ServiceDiscoveryProtocol

The Linux command for browsing services with SDP is sdptool browse <addr>.

 #!/usr/bin/python 2 3 import bluetooth 4 import sys 5 6 if len(sys.argv) < 2: 7 print "Usage: " + sys.argv[0] + " <addr>" 8 sys.exit(0) 9 10 services = bluetooth.find_service(address=sys.argv[1]) 11 12 if(len(services) < 1): 13 print "No services found" 14 else: 15 for service in services: 16 for (key, value) in service.items(): 17 print key + ": " + str(value) 18 print "" 
If you wouldlike to send self-constructed802.11packets into a Wiﬁ net you need a driverthat allows packetinjectionanda compatiblechipset. Atherosis the common choice, but others are possible too. Depending on the chipset, you have to choose a driver such as Hostap, MadWiﬁ, Ath5k or Ath9k.
8.12 Playing Wiﬁ Client 125
Youcanﬁndoutthechipsetofyourdevicebyexecutingthecommandlspcior lsusb dependingwhether it is an internal card or USB stick. If you do not get any useful informationat all, you are either not root or you should consult the output of the commanddmesg. 

airmon-ng start wlan0 aireplay-ng --test mon0
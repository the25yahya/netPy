from scapy.all import *


class Sniff :
    def __init__(self) :
        self.sniffing = False
    def capture(self,filters):
            self.sniffing = True
            if self.sniffing and filters:
                try :
                    sniff(filter=filters,iface=conf.iface,prn=lambda x: x.summary(),count=0)
                except KeyboardInterrupt :
                     self.sniffing = False                 
            if self.sniffing :
                try :
                    sniff(iface=conf.iface,prn=lambda x : x.summary(),count=0)
                except KeyboardInterrupt :
                     self.sniffing = False 
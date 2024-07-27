from scapy.all import *


class Sniff :
    def __init__(self,filters,interface) :
        self.filters = filters
        self.interface = interface

    def capture(self):
        if self.interface and self.filters :
            sniff(filter=self.filters,iface=self.interface,prn=lambda x: x.summary(),count=0)
        else :
            sniff(prn=lambda x: x.summary(),count=0)
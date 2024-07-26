# basic ping scans to determine wether the host is up
# recursive mode 
# basic cidr subnet scan 
# os detection
from scapy.all import *
import ipaddress
import threading


class Network_Scan:
    def __init__(self,cidr):
        self.cidr = ipaddress.ip_network(cidr, strict=False)
        self.hosts = [str(ip) for ip in self.cidr.hosts()]
    def scan_network(self):
        threads = []
        for ip in self.hosts:
            host_scan = Host_Scan(ip)
            t = threading.Thread(target=host_scan.host_scan)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
      

class Host_Scan:
    def __init__(self,target) :
        self.target = target
    def host_scan(self):
        packet = IP(dst=self.target)/ICMP()
        response = sr1(packet,timeout=1,verbose=0)
        if response :
            icmp_layer = response.getlayer(ICMP)
            icmp_type = icmp_layer.type
            icmp_code = icmp_layer.code
            if icmp_code == 0 and icmp_type == 0 :
                print(f"host reachable : {self.target}") 
                print(response)
    

    def Os_detection(self):
        print(":)")
from scapy.all import *
import ipaddress
import threading
import socket



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
                return True
            
    def probe_port(self,port) :
        syn_packet = IP(dst=self.target) / TCP(dport=int(port),flags='S')
        response = sr1(syn_packet,timeout=1,verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags == 'SA' :
            print(f"PORT OPEN : {port}")
            return True

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
      




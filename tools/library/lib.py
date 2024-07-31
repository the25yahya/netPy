import uuid
import subprocess
from scapy.all import *


def get_mac_adress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac_adress = ":".join([mac[e:e+2] for e in range(0,11,2)])
    print(mac_adress
          )
    return mac_adress

def arp_cash(ip):
    # Run the arp-scan command and capture the output
    cash = subprocess.run(
        f"arp-scan --interface {conf.iface} {ip}/24 --plain", 
        shell=True, 
        stdout=subprocess.PIPE, 
        text=True, 
        stderr=subprocess.PIPE
    )
    
    # Print the raw output (for debugging purposes)
    print(cash.stdout)
    
    # Dictionary to store the IP-MAC pairs
    arp_dict = {}
    
    # Regular expression to match IP and MAC addresses
    regex = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]+)')
    
    # Apply the regex to each line of the output
    for line in cash.stdout.splitlines():
        match = regex.match(line)
        if match:
            ip_address = match.group(1)
            mac_address = match.group(2)
            arp_dict[ip_address] = mac_address
        
    return arp_dict

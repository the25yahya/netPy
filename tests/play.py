from scapy.all import * 

def eapol_callback(packet):
    if packet.haslayer(EAPOL):
        print("EAPOL packet detected")
        packet.show()

# Sniff for EAPOL frames and capture the AP's MAC address
sniff(iface="Wi-Fi", prn=eapol_callback)
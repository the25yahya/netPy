from scapy.all import IP, ICMP, sr1

# Define the network
network = "192.168.1.0/24"

# Create an IP object with the network as the destination
ip = IP(dst=network)
print(ip)  # Shows the IP object with the network

# Iterate over the generated IP packets for each IP address in the network
for packet in ip:
    # Print the packet to see the individual IP packets
    print(packet)

    # Create an ICMP packet for each IP address
    icmp_packet = packet / ICMP()

    # Send the packet and wait for a response
    response = sr1(icmp_packet, timeout=1, verbose=False)

    # Check if there was a response
    if response:
        print(response.summary())

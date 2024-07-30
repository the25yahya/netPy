import argparse
from tools import Host_Scan,Network_Scan,Sniff,ARP
from library import tcp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="probe, scan, get shells, transfer files, just like netcat"
    )


subparser = parser.add_subparsers(dest="mode",help="modes")

#scan parser
scan_parser = subparser.add_parser('scan',help='scan a host or a network subnet')
scan_parser.add_argument('-H','--host',help='host ip adresss to scan')
scan_parser.add_argument('-N','--network',help='CIDR notation')
scan_parser.add_argument('-r','--recursive',action='store_true',help='start a recursive scan')
scan_parser.add_argument('-p','--port',help='probe open ports')
scan_parser.add_argument('-B','--banner',action='store_true',help='grab banner')

#sniffer parser
sniff_parser = subparser.add_parser('sniff',help='sniff packets on a network')
sniff_parser.add_argument('-I','--interface',help='interface to sniff packets')
sniff_parser.add_argument('-P','--protocol',type=str,help='protocol to sniff packets of , ex : -P http')
sniff_parser.add_argument('--dst',type=str,help='only sniff packets going to a certain destination')
sniff_parser.add_argument('--src',type=str,help='only sniff packets coming from a specific source')

#attack parser
attack_parser = subparser.add_parser('attack',help='perform various wireless attacks')
attack_parser.add_argument('--arp',action='store_true',help='''
--spoof (arp spoofing attack)
--wifi (perform various wifi attacks including deauthentication attacks - attention : promiscuous mode is neccessary
                            for some attacks!)                       
''')
attack_parser.add_argument('--dst_IP',help='target ip adress')
attack_parser.add_argument('--dst_MAC',help='target mac adress')
attack_parser.add_argument('--gateaway',help='gateaway adress')
attack_parser.add_argument('--dos',action='store_true',help='flood a host with arp poison attacks causing denial of service')



args = parser.parse_args()

if args.mode == 'scan':
    if args.host :
        host = Host_Scan(args.host)
        if args.recursive:
          while True:
            host.host_scan()
        else :
           host.host_scan()
    if args.host and args.port :
       host = Host_Scan(args.host)
       if host.host_scan() :
          host.probe_port(args.port)

    if args.network : 
        network = Network_Scan(args.network)
        network.scan_network()
    if args.banner :
       client = tcp.tcpClient(args.host,args.port)
       client.connect()
       banner = client.grab_banner()
       print(banner)
       client.close()
if args.mode == 'sniff':
    filters = []
    arguments = [args.dst,args.src,args.protocol]
    for argument in arguments:
       if argument:
          filters.append(argument)
    filter_string = ' and '.join(filters)
    print(filter_string)

if args.mode == 'attack':
   if args.arp :
      arp = ARP(args.dst_IP,args.dst_MAC,args.gateaway)
      if args.arp and args.dos :
         arp.dos()
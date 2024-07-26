import argparse
from tools import Host_Scan,Network_Scan

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

#sniffer parser
sniff_parser = subparser.add_parser('sniff',help='sniff packets on a network')
sniff_parser.add_argument('-I','--interface',help='interface to sniff packets')
sniff_parser.add_argument('-P','--protocol',help='protocol to sniff packets of , ex : -P http')

args = parser.parse_args()

if args.mode == 'scan':
    if args.host :
        host = Host_Scan(args.host)
        if args.recursive:
          while True:
            host.host_scan()
        else :
           host.host_scan()

    if args.network : 
        network = Network_Scan(args.network)
        network.scan_network()

if args.mode == 'sniff':
    print(f"sniff : {args.protocol} of {args.interface}")
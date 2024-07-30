import socket
from scapy.all import *
from library import tcp


server = tcp.tcpServer(ip,port,clients)


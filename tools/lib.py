import uuid
import subprocess


def get_mac_adress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac_adress = ":".join([mac[e:e+2] for e in range(0,11,2)])
    print(mac_adress
          )
    return mac_adress

def arp_cash():
    cash = subprocess.run("arp -a",shell=True,stdout=subprocess.PIPE,
                                   text=True,stderr=True)
    print(cash.stdout)

if __name__ == '__main__' :
    arp_cash()
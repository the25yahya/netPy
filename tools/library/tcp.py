import socket
from sys import argv
import telnetlib


class tcpClient:
    def __init__(self,ip,port):
        self.ip = str(ip)
        self.port = int(port)
        self.client = None
    def connect(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try : 
            self.client.connect((self.ip,self.port))
            print(f"[*] connected to {self.ip}:{self.port}")
        except socket.error as error:
            print(f"[*] error connecting to {self.ip}:{self.port} - {error}")
            self.client = None
    
    def send_request(self,data):
        if self.client:
            try:
                self.client.sendall(data.encode())
                print(f"[*] sent {data} to {self.ip}:{self.port}")
                response = self.client.recv(4096)
                print(response.decode())
            except socket.error as error:
                print(f"[*] error sending data : {error}")
        
        else:
            print(f"[*] not connected to {self.ip}:{self.port}")

    def grab_banner(self):
        if self.client:
          try :
             banner = self.client.recv(1024)
             return banner.decode().strip()
          except Exception as e :
             print(f"An erro has occured : {str(e)}")
        else:
             print(f"[*] Not connected to {self.ip}:{self.port}")
             return None

    def close(self):
        if self.client:
          self.client.close()
          print(f"[*] connection to {self.ip}:{self.port} terminated")
          self.client=None


class tcpServer:
    def __init__(self,ip,port,clients):
        self.ip = ip
        self.port = int(port)
        self.clients = int(clients)
        self.server_socket = None
        self.threads = []
    
    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.ip,self.port))
        self.server_socket.listen(self.clients)
        print(f"[*] started tcp server at {self.ip}:{self.port}")

        def handle_client(client):
            with client_socket:   
                while True:
                    try:
                      data = client.recv(1024)
                      if not data:
                          break
                      print(f"[*] received data : {data}")
                      client.sendall(data)
                    except socket.error as e:
                        print(f"[*] error handling client : {e}")
        while True :
            try:
                client_socket, client_adress = self.server_socket.accept()
                print(f"[*] accepted connection from : {client_adress[0]}:{client_adress[1]}")
                client_handler = threading.Thread(target=handle_client,args=(client_socket,))
                client_handler.start()
                self.threads.append(client_handler)
            except socket.error as e :
                print(f"[*] error accepting connection: {e}")
    
    def close_server(self):
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None
            print(f"[*] server at {self.ip}:{self.port} closed")
        for t in self.threads:
            t.join()


if __name__ == '__main__' :
    script, ip, port, clients = argv
    try :
        server = tcpServer(ip,int(port),int(clients))
        server.start_server()
    except KeyboardInterrupt :
        server.close_server()
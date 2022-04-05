'''
UDP Client Keep Alive - The client interface used to 'ping' the target device (UDP server).
'''

import socket
import time as t

class KeepAlive:
    def __init__(self, udp_ip, udp_port, msg_str):
        
        self.udp_ip =  udp_ip     # UDP_IP = "localhost" (loopback IP address for testing)
        self.udp_port = udp_port  # UDP_PORT = 5005
        self.msg_str = msg_str    # "Hello, World!"
        self.msg_count = 0        # Message counter

        print (f"UDP target IP: {udp_ip}")
        print (f"UDP target port: {udp_port}")
        print (f"message: {msg_str}")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4 and UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow address/port reuse immediately 


    def hello(self): # this method is invoked as a thread
        while True: 
                self.sock.sendto(bytes(self.msg_str, 'utf-8'), (self.udp_ip, self.udp_port))
                self.msg_count = self.msg_count + 1
                data, addr = self.sock.recvfrom(1024)
                print(f"Client: message {data} received from server")
                t.sleep(1)

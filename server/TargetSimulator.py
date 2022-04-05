'''
Target Simulator - Simulates a target system (Server) that Target Manager Client is 'talking' to.
'''
import socket
import time as t

class TargetSimulator:

    def __init__(self, udp_ip, udp_port):
        self.udp_ip =  udp_ip     # UDP_IP = "localhost" (loopback IP address for testing)
        self.udp_port = udp_port  # UDP_PORT = 5005
        self.msg_count = 0        # Message counter

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # IPv4 and UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow address/port reuse immediately 
        # self.sock.setblocking(0)   # play with receiver blocking enable/disable
        # self.sock.settimeout(0.3)                       
        self.sock.bind((udp_ip, udp_port))

    def get_receive_counts(self):
        return self.msg_count

    def receiver(self):  # this method is invoked as a thread 
        while True:
                data, addr = self.sock.recvfrom(1024)
                self.msg_count = self.msg_count + 1
                print (f"Server: message {self.msg_count} received from client")
                self.sock.sendto(str.encode(str(self.msg_count)), addr)

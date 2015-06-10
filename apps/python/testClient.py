import socket
import sys
import time

HOST, PORT = "localhost", 18149
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while (True):
    #ctrl-c to exit
    data = "req\n"
    sock.sendto(data.encode(), (HOST, PORT))
    received = sock.recv(1024)
    print ("Received: {}".format(received.decode()))
    time.sleep(1)

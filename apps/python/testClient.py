import socket
import sys

HOST, PORT = "localhost", 18149
data = "req_data\n"

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(data.encode(), (HOST, PORT))
received = sock.recv(1024)

print ("Sent:     {}".format(data))
print ("Received: {}".format(received.decode()))

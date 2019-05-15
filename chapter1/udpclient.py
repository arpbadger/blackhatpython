## udpclient is a python tcp client tool developed by arpbadger with assistance from Justic Seitz, "Black Hat Python"

import socket 

target_host = "127.0.0.1"
target_port = 80

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("ABCDEFG", (target_host,target_port))

#receive some data
data,addr = client.recvfrom(4069)

print data

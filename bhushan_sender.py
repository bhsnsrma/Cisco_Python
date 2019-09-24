#!/usr/bin/python3

import socket,time

#checking for socket functions

print([i for i in dir(socket) if 'socket' in i])

#creating UDP socket
# ipv4 socket -- ipv4(6byte) + 2byte
# ipv6 socket -- ipv6(16 byte) + 2byte

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # for UDP
#                   for ipv4    for UDP socket
#socket.socket(socket.AF_INET,socket.SOC_STREAM)  # for TCP
#                   for ipv4    for TCP port
#for sender:
while True:
#enter message
    msg=input("Enter data to send : ")
#converting data into byte-like string
    newmsg=msg.encode('ascii')
#Let's send messageto target
    s.sendto(newmsg,("127.0.0.1",8899))
    data=s.recvfrom(1000)
    print(data)
#
#
# for receiver only
#s.bind("",8899)
#bind will accep tuple format ip & port
#while True :
#data=s.recvfrom(1000) # this is the buffer size
#print(data[0])
#print("sender address is ",data[1])
#msg=input(enter reply : ")
#newmsg=msg.encode('ascii')
#s.sendto(newmsg,data[1])
#s.close()


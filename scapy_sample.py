from socket import IPV6_RECVPATHMTU
from telnetlib import IP
from scapy.all import *

# 参考
# https://qiita.com/Howtoplay/items/4080752d0d8c7a9ef2aa

icmp = ICMP(code=2)
icmp.show()

arp = ARP()
arp.show()

ls(IP)

from scapy.all import *

# LAN内のMACアドレスとIPアドレスを調べる
ans, unans = srp(
    Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.50.234/24"), timeout=2
)
ans.summary(lambda k_v: k_v[1].sprintf("%Ether.src% %ARP.psrc%"))
print("====")
unans.summary()

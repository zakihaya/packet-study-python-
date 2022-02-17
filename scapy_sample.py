from scapy.all import *

# 参考
# https://qiita.com/Howtoplay/items/4080752d0d8c7a9ef2aa

# print("====")
# arp = ARP()
# arp.show()
# print("====")
# ls(ARP)
# print("====")
# ls(Ether)
# print("====")
# ls(IP)

# Googleにpingを送信する
# / で区切ってパケットを生成する
# 下のping変数は、IPヘッダとICMPヘッダ
ping = IP(dst="www.google.com") / ICMP()
# sr1 - レイヤ3でパケットを送信し，その応答の1つ目がレスポンスとして返ってくる
ans = sr1(ping)
ans.show()

print("==========")

# 特定のIPアドレスのMACアドレスを得るためのARP要求を行う
arp = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.50.174")
# srp1 - レイヤ2でパケットを送信する、pが入っているメソッドはレイヤ2でパケットを扱う
res = srp1(arp)
res.show()

from scapy.all import *
ans, _ = sr(IP(dst="192.168.63.131")/TCP(dport=80, flags="S"), timeout=2)

for sent, recv in ans:
    print(f"Window Size: {recv[TCP].window}")
    print(f"Options: {recv[TCP].options}")

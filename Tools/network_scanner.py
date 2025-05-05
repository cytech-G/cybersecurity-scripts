from scapy.all import ARP, Ether, srp

target_ip = "192.168.63.0/24"
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)
result = srp(packet, timeout=2, verbose=False)[0]

for sent, received in result:
    print(f"IP: {received.psrc} - MAC: {received.hwsrc}")

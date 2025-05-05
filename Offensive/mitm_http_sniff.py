from scapy.all import *
from scapy.layers.http import HTTPRequest

def sniff_http(packet):
    if packet.haslayer(HTTPRequest):
        host = packet[HTTPRequest].Host.decode()
        path = packet[HTTPRequest].Path.decode()
        print(f"[*] HTTP Request >> {host}{path}")
        if packet.haslayer(Raw):
            print(packet[Raw].load.decode(errors="ignore"))

print("[*] Sniffing started...")
sniff(filter="tcp port 80", prn=sniff_http, store=False)

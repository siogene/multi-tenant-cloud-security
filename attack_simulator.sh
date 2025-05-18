#!/bin/bash
echo "Starting simulated SSH brute-force attack..."
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://localhost

echo "Running simulated port scan with Nmap..."
nmap -T4 -A -v localhost

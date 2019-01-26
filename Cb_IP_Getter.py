import re
import sys

print("Input IP's from CB")

IPs = open('IPs.txt', 'r')

ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', IPs)
print(*ip, sep='\n')

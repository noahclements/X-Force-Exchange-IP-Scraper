import re

ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', open('rawIPs.txt', 'r').read())

file = open('cleanIPs.txt', 'w')
for line in ip:
    file.write(line + '\n')
file.close()

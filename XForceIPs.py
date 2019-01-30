import requests
import json
import base64
import re

def send_request(apiurl, scanurl, headers, count):
    fullurl = apiurl +  scanurl
    response = requests.get(fullurl, params='', headers=headers, timeout=20)
    all_json = response.json()
    score = int(all_json['score'])
    if score > 4:
        ip = all_json['ip']
        print(ip)
        print(score)
    else:
        print("not a threat", count)

# this copies in the raw data from site, and put's the IPs into an array
findIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', open('rawIPs.txt', 'r').read())

ipList = []
for line in findIP:
   ipList.append(line)



key = '6c270482-aa75-46b6-a65b-3e94379dedae'
password = 'db62ca96-015c-4f26-a34c-54e43f4b2301'

data_string = key + ":" + password
data_bytes = data_string.encode('utf-8')

token = base64.b64encode(data_bytes).decode('ascii')
headers = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
XForce_url = "https://api.xforce.ibmcloud.com:443"

count = 0
for url in ipList:
    count += 1
    apiurl = XForce_url + "/ipr/"
    send_request(apiurl, url, headers, count)

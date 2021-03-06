import requests
import json
import base64
import re
import ipaddress

def send_request(apiurl, scanurl, headers, count):
    fullurl = apiurl +  scanurl
    try:
        response = requests.get(fullurl, params='', headers=headers)
        response.raise_for_status()
        all_json = response.json()
        score = int(all_json['score'])
        if score > 4:
            ip = all_json['ip']
            print(ip + "\n" + str(score))
            with open("flaggedIPs.txt", "a") as flaggedIP:
              flaggedIP.write(ip + "\n" + str(score) + "\n")
        else:
            print("not a threat", count)
    except requests.exceptions.HTTPError as err:
        print(err)
    

# this copies in the raw data from site, and put's the IPs into an array
findIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', open('rawIPs.txt', 'r').read())


ipList = []
for line in findIP:
  if (ipaddress.ip_address(line).is_private) == False:
    if line not in ipList:
      ipList.append(line)



key = '<api key here>'
password = '<password here>'

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

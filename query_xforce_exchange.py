import requests
import urllib3
import sys
import json
from optparse import OptionParser
import hashlib
import base64

def send_request(apiurl, scanurl, headers):
    fullurl = apiurl +  scanurl
    response = requests.get(fullurl, params='', headers=headers, timeout=20)
    all_json = response.json()
    score = int(all_json['score'])
    if score > 4:
    	ip = all_json['ip']
    	print ip
    	print score
    else:
    	print "not a threat"



key = "<api key here>" 
password ="<password here>"

token = base64.b64encode(key + ":" + password)
headers = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
XForce_url = "https://api.xforce.ibmcloud.com:443"
 
URL_File = open('IPs.txt', 'r')

for url in URL_File:
	apiurl = XForce_url + "/ipr/"
	send_request(apiurl, url, headers)

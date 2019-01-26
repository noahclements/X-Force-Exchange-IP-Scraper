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
    print json.dumps(all_json, indent=4, sort_keys=True) 


key = "<api key here>" 
password ="<password here>"

token = base64.b64encode(key + ":" + password)
headers = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
url = "https://api.xforce.ibmcloud.com:443"
 
scanurl = raw_input("Enter an IP Address to scan")

apiurl = url + "/ipr/"
send_request(apiurl, scanurl, headers)

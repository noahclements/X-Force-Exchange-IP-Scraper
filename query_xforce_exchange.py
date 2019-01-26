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

def get_md5(filename):
    try:
        f = open(filename,"rb")
        md5 = hashlib.md5((f).read()).hexdigest()
        return md5
    except e:
        print str(e)

if __name__ == "__main__":
    key = "<api_key_here>" 
    password ="password_here>"

    token = base64.b64encode(key + ":" + password)
    headers = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
    url = "https://api.xforce.ibmcloud.com:443"


    parser = OptionParser()
    
    parser.add_option("-i", "--ip", dest="s_ip" , default=None,
                      help="ip to be checked", metavar="ipaddress")
(options, args) = parser.parse_args()


if (options.s_ip is not None):
    scanurl = options.s_ip
    apiurl = url + "/ipr/"
    send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/history/"
    send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/malware/"
    send_request(apiurl, scanurl, headers)


if len(sys.argv[1:]) == 0:
  parser.print_help()

if ( options.s_url is not None ):
    apiurl = url + "/url/"
    scanurl = options.s_url
    send_request(apiurl, scanurl, headers)
elif ( options.m_url is not None ):
    apiurl = url + "/url/malware/" 
    scanurl = options.m_url
    send_request(apiurl, scanurl, headers)
elif ( options.s_cve is not None ):
    apiurl = url + "/vulnerabilities/search/" 
    scanurl = options.s_cve
    send_request(apiurl, scanurl, headers)
elif (options.s_ip is not None):
    scanurl = options.s_ip
    apiurl = url + "/ipr/"
    send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/history/"
    send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/malware/"
    send_request(apiurl, scanurl, headers)
elif (options.malfile is not None ):
    md5 = get_md5(options.malfile)
    if md5:
        send_request(url+"/malware/", md5, headers)
elif (options.s_xfid is not None ):
    send_request(url+"/vulnerabilities/", options.s_xfid, headers)
elif (options.hash is not None ):
    send_request(url+"/malware/", options.hash, headers)

if len(sys.argv[1:]) == 0:
    parser.print_help()

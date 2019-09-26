#!/usr/bin/python3

import requests

from requests.auth import HTTPBasicAuth
# this is for supplying asic http authentication
cred=HTTPBasicAuth('root','cisco')
h={'Accept' : 'applicaition/json'}
#h={'Accept':'text/html'}
#defining data from that api in JSON format
url='http://192.168.176.128/level/15/exe/-/sh/ip/int/br/CR'


# now connection to restconf OR HTTP Protocol
output=requests.get(url,headers=h,auth=cred)
print(output)

#only givin HTTP respnse code
print(output.text)
# Giving HTML based 

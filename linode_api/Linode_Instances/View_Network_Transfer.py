#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import math
import sys
from urllib import parse,request
 

LINODE_ID = ''
LINODE_TOKEN_RO = ''
 

def getTransfer(linode_id, argv):
    url = 'https://api.linode.com/v4/linode/instances/' + linode_id + '/transfer'
    header_dict = {
        'User-Agent': 'User-Agent: curl/7.68.0',
        'Authorization': 'Bearer ' + LINODE_TOKEN_RO}
 
    req = request.Request(url, headers=header_dict)
    res = request.urlopen(req)
    ret = res.read()
 
    jsonData = json.loads(ret)
    transfer_quota = float(round(jsonData['quota'], 2))
    transfer_used = round(jsonData['used'] / math.pow(1024, 3), 2)
 
    if argv == 'quota':
        print(transfer_quota)
    if argv == 'used':
        print(transfer_used)
    if argv == 'percent':
        print(round(float(transfer_used / transfer_quota * 100), 1))
 

def main():
    getTransfer(LINODE_ID, sys.argv[1])
 

if __name__ == '__main__':
    main()
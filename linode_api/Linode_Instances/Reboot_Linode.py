#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
from urllib import request
 
LINODE_API_VER = 'v4'
LINODE_ID = ''
LINODE_TOKEN_RW = ''
 

def reboot(linode_id):
    url = 'https://api.linode.com/' + LINODE_API_VER + '/linode/instances/' + linode_id + '/reboot'
    header_dict = {
        'User-Agent': 'curl/7.68.0',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + LINODE_TOKEN_RW
    }
 
    req = request.Request(url, headers=header_dict, method='POST')
    res = request.urlopen(req, timeout=10)
    ret = res.read()
 
    jsonData = json.loads(ret)
 
    print(jsonData)
 

def main():
    opt = str(input('Reboot Linode (ID:' + LINODE_ID + ')? (y/N) ').strip())
    if opt == 'y' or opt == 'Y':
        print('Rebooting ...')
        reboot(LINODE_ID)
    else:
        print('Reboot Cancelled.')
 

if __name__ == '__main__':
    main()

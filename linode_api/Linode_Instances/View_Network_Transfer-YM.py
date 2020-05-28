#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import sys
from urllib import request
 
LINODE_API_VER = 'v4'
LINODE_ID = ''
LINODE_TOKEN_RO = ''
 

def getTransfer(linode_id, year, month):
    url = 'https://api.linode.com/' + LINODE_API_VER + '/linode/instances/' + linode_id + '/transfer' + '/' + year + '/' + month
    header_dict = {
        'User-Agent': 'curl/7.68.0',
        'Authorization': 'Bearer ' + LINODE_TOKEN_RO
    }
 
    req = request.Request(url, headers=header_dict)
    res = request.urlopen(req, timeout=10)
    ret = res.read()
 
    jsonData = json.loads(ret)
    print(jsonData)

    #transfer_quota = float(round(jsonData['quota'], 2))
    #transfer_used = round(jsonData['used'] / pow(1024, 3), 2)
 
    #if argv == 'quota':
    #    print(transfer_quota)
    #elif argv == 'used':
    #    print(transfer_used)
    #elif argv == 'percent':
    #    print(round(float(transfer_used / transfer_quota * 100), 1))
    #else:
    #    print('Invalid argument!')
 

def main():
    flag = True

    while flag:
        year_month = str(input('Input year+month (e.g. 202108): ').strip())
        year = year_month[:4]
        month = year_month[4:]

        if not year_month.isdigit():
            print('Integer digitals only!')

        elif len(year_month) < 5 or len(year_month) > 6:
            print('Year must be 4-digital!')

        elif int(year) < 2000 or int(year) > 2037:
            print('Year must be between 2000-2037!')

        elif int(month) < 1 or int(month) > 12:
            print('Month must be between 1-12!')

        else:
            flag = False

    if len(month) == 1:
        month = '0' + month

    getTransfer(LINODE_ID, year, month)
 

if __name__ == '__main__':
    main()

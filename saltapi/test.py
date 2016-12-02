#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import saltapi
import time

from var_dump import var_dump


def test():
    print 'ok!\n'

SALTAPI_HOST = 'https://172.31.31.1'
SALTAPI_PORT = 8388
SALTAPI_USER = 'saltapi'
SALTAPI_PASS = 'llw838'
SALTAPI_VSSL = False

api = saltapi.SaltAPI(SALTAPI_HOST, SALTAPI_PORT, SALTAPI_USER, SALTAPI_PASS, SALTAPI_VSSL)

request = {
    'tgt':'centos7.inanu.net',
    'fun':'sysinfo.dtime',
    #'arg':'',
}

res = api.do(request)

print res

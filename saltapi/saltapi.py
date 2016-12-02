#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import threading
import urllib
import urllib2
import cookielib
import ssl
import json


class SaltAPI(object):
    def __init__(self, api_host, api_port, api_user, api_pass, ssl_verify=True):
        '''
        Login and get token.
        '''
        if not ssl_verify:
            ssl._create_default_https_context = ssl._create_unverified_context

        self.saltapi_url = ':'.join([str(api_host), str(api_port)])

        path = '/login'

        request = {
            'username':api_user,
            'password':api_pass,
            'eauth':'pam',
        }

        res = self.do(request, path)

        self.token = json.loads(res)['return'][0]['token'].encode('utf-8')

    def do(self, request, path=''):
        '''
        Process request.
        '''
        if path == '/login':
            head_data = {
                'Host':self.saltapi_url,
                'Accept':'application/json',
            }

            post_data = {}

        else:
            head_data = {
                'Host':self.saltapi_url,
                'Accept':'application/json',
                'X-Auth-Token':self.token,
            }

            post_data = {
                'client':'local',
            }

        for key in request.keys():
            post_data[key] = request[key]

        post_data = urllib.urlencode(post_data)

        req_url = ''.join([str(self.saltapi_url), str(path)])

        req = urllib2.Request(req_url, data=post_data, headers=head_data)

        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

        ret = opener.open(req).read()

        return ret


if __name__ == '__main__':
    raise SystemExit()

#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

def hex_to_int(ip):
    length = len(ip)
    step = 2

    i = 0
    ip_int = []
    while i < length:
        ip_section = int(ip_hex[i:i+step], 16)
        ip_int.append(str(ip_section))
        i += 2

    ip_int.reverse()

    return '.'.join(ip_int)


ip_hex = 'C80111AC'

print hex_to_int(ip_hex)

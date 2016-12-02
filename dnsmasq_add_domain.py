#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import os
import re
import sys


def find_conf():
    CONF = '/usr/local/dnsmasq/etc/dnsmasq.conf'

    if not os.path.exists(CONF):
        if os.path.exists('/etc/dnsmasq.conf'):
            CONF = '/etc/dnsmasq.conf'
        elif os.path.exists('/usr/local/etc/dnsmasq.conf'):
            CONF = '/usr/local/etc/dnsmasq.conf'
        else:
            raise SystemExit('Can not found Dnsmasq config file!')

    return CONF


def group_list(CONF):
    groups = []

    try:
        conf_fd = open(CONF, 'r')

    except Exception as e:
        raise SystemExit(e)

    try:
        for line in conf_fd:
            match = re.findall(r'^#\s(.*)', line)
            if match:
                groups.append(match[0])

    except Exception as e:
        print e

    finally:
        conf_fd.close()

    table_head = 'All Domain Groups'
    print '\n' + table_head
    print '=' * len(table_head)
    if len(groups) > 0:
        for group in groups:
            print '* ' + group
    else:
        print 'No group in config file!'


def add_domain(CONF, RECORD_IP, domain, group=''):
    try:
        if group:
            conf_fd = open(CONF, 'w+')
        else:
            conf_fd = open(CONF, 'a')

    except Exception as e:
        raise SystemExit(e)

    if domain[0] == '.':
        domain = domain[1:]

    record = 'address=/.' + str(domain) + '/' + str(RECORD_IP)

    try:
        conf_fd.write(record)

    except Exception as e:
        print e

    finally:
        conf_fd.close()


def main():
    RECORD_IP = '172.31.31.2'
    CONF = find_conf()

    if len(sys.argv) == 1:
        groups = group_list(CONF)

    elif len(sys.argv) == 2:
        domain = sys.argv[1]
        add_domain(CONF, RECORD_IP, domain)

    elif len(sys.argv) > 3:
        raise SystemExit('Too many arguments!')


if __name__ == '__main__':
    main()

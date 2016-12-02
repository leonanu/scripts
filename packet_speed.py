#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import time
import datetime
import psutil
import commands


if os.geteuid() != 0:
    raise SystemExit('You must be root!')


# Packet detect interval.
# Unit: Second
INTERVAL = 3

# When exceed this packet speed, trigger inspect actions.
# Unit: packets/s
TRIGGER_PKG_SPEED = 2000

# tcpdump packets capture number.
# Unit: packet
PACKET_CAPTURE = 1000

# tcpdump output cap file path
OUTPUT_PATH = '/var/log'


def packet_dump(nic):
    nic_address = psutil.net_if_addrs()[nic][0].address

    now = datetime.datetime.now()
    format_time = now.strftime('%Y-%m-%d_%H-%M-%S')
    filename = OUTPUT_PATH + '/' + nic + '_' + nic_address + '_' + str(format_time) + '.cap'

    cmd = 'tcpdump -i ' + nic + ' -s 0 -c ' + str(PACKET_CAPTURE) + ' -nn -w ' + filename

    commands.getstatusoutput(cmd)


def packet_calc(interval):
    nic_list = psutil.net_io_counters(pernic=True).keys()

    netio1 = psutil.net_io_counters(pernic=True)
    time.sleep(INTERVAL)
    netio2 = psutil.net_io_counters(pernic=True)

    for nic in nic_list:
        packets_sent_avg = (netio2[nic].packets_sent - netio1[nic].packets_sent) / INTERVAL
        packets_recv_avg = (netio2[nic].packets_recv - netio1[nic].packets_recv) / INTERVAL

        if packets_sent_avg >= TRIGGER_PKG_SPEED:
            packet_dump(nic)


def main():
    nic_list = psutil.net_io_counters(pernic=True)
    print nic_list['lo']
    print type(nic_list['lo'])
    sys.exit(0)
    packet_calc(INTERVAL)


if __name__ == '__main__':
    main()

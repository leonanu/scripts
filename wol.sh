#!/bin/bash

NIC_FACE='eth0'
MAC_ADDR='90:2B:34:32:37:94'

/usr/sbin/ether-wake -D -i ${NIC_FACE} ${MAC_ADDR}

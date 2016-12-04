#!/bin/sh

ipaddr='172.16.1.1'
netmask='255.255.255.0'
gateway='172.16.1.255'

echo "alias bond0 bonding" > /etc/modprobe.d/bonding.conf

#echo "------------------------"

echo 'DEVICE="em2"
BOOTPROTO="none"
USERCTL=no
ONBOOT="yes"
MASTER="bond0"
SLAVE="yes"' > /etc/sysconfig/network-scripts/ifcfg-em2


#echo "------------------------"

echo 'DEVICE="em1"
BOOTPROTO="none"
USERCTL=no
ONBOOT="yes"
MASTER="bond0"
SLAVE="yes"'  > /etc/sysconfig/network-scripts/ifcfg-em1


#echo "------------------------"

echo "DEVICE=\"bond0\"
TYPE=\"Ethernet\"
IPADDR=$ipaddr
NETMASK=$netmask
GATEWAY=$gateway
ONBOOT=\"yes\"
BOOTPROTO=\"none\"
USERCTL=\"no\"
BONDING_OPTS=\"mode=0 miimon=100\"" >  /etc/sysconfig/network-scripts/ifcfg-bond0


#service network restart

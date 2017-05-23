#!/bin/bash

systemctl stop dnsmasq.service
sleep 1
systemctl stop nscd.service

systemctl restart network.service

systemctl start nscd.service
sleep 1
systemctl start dnsmasq.service

systemctl status nscd.service
sleep 1
systemctl status dnsmasq.service

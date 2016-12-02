#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

from daemon import Daemon
import time
import sys

class foo(Daemon):
    def run(self):
        while True:
            print '#'*50
            time.sleep(1)

p = foo(pidfile='/tmp/aaa.pid', stdout='/dev/stdout')
if sys.argv[1] == 'start':
    p.start()

elif sys.argv[1] == 'stop':
    p.stop()

elif sys.argv[1] == 'status':
    p.is_running()

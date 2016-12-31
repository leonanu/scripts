#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

count = int(raw_input('The number of elements: '))

mydict = {}

for i in range(count):
    value = hex(random.randint(0, count))

    current_value = []
    for k in mydict.keys():
        current_value.append(mydict[k])

    while value in current_value:
        value = hex(random.randint(0, count))

    mydict[i] = value


print mydict

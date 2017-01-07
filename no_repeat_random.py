#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


LIMITATION = 1000000

count = int(raw_input('How many random integer number you want? '))

lst_random = []

if count == LIMITATION:
    for i in range(0, count):
        lst_random.append(i)

elif count < LIMITATION:
    for i in range(count):
        value = random.randint(0, LIMITATION)

        while value in lst_random:
            value = random.randint(0, LIMITATION)

        lst_random.append(value)

else:
    error = '\nError!\nYour want %d random number, but the random number LIMITATION is %d.' % (count, LIMITATION)
    raise SystemExit(error)

print lst_random

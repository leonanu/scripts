#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


RND_RANGE = 100

count = int(raw_input('How many random integer number you want? '))

lst_random = []

for i in range(count):
    value = random.randint(0, RND_RANGE)

    while value in lst_random:
        value = random.randint(0, RND_RANGE)

    lst_random.append(value)


print lst_random

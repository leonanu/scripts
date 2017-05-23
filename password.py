#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import sys


class Password(object):
    def __init__(self, action, password):
        self.action = action
        self.password = password

    def run(self):
        res = []
        for i in self.password:
            if i.isalpha():
                res.append(self.alpha(i))
            elif i.isdigit():
                res.append(self.digit(i))
            else:
                res.append(i)

        res = ''.join(res)

        return res

    def alpha(self, element):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        is_upper = False

        if element.isupper():
            is_upper = True
            element = element.lower()

        index_ori = alphabet.index(element)

        if self.action == 'dec':
            if index_ori < 25:
                index_res = alphabet.index(element) + 1
            else:
                index_res = 0

        elif self.action == 'enc':
            if index_ori > 0:
                index_res = alphabet.index(element) - 1
            else:
                index_res = 25

        if is_upper:
            element_res = alphabet[index_res].upper()
        else:
            element_res = alphabet[index_res]

        return element_res

    def digit(self, element):
        element = int(element)

        if self.action == 'dec':
            if element == 9:
                element_res = 0
            else:
                element_res = element + 1

        elif self.action == 'enc':
            if element == 0:
                element_res = 9
            else:
                element_res = element - 1

        return str(element_res)


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Parameter Error!')

    action = sys.argv[1]
    if action != 'dec' and action != 'enc':
        raise SystemExit('Action must be \'enc\' or \'dec\' only!')

    password = sys.argv[2]

    p = Password(action, password)

    print p.run()
    

if __name__ == '__main__':
    main()

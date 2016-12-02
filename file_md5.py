#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import os
import hashlib

def dir_walk(base_dir):
    for parent_dir, dirnames, filenames in os.walk(base_dir):

        for filename in filenames:
            yield os.path.join(parent_dir, filename)


def file_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def main():
    root_dir = '/usr/local/python2.7'
    files = dir_walk(root_dir)

    md5_list = []
    for fname in iter(files):
        md5 = file_md5(fname)
        md5_list.append((fname, md5))

    print md5_list


if __name__ == '__main__':
    main()

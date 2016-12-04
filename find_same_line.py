#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import sys


def find_same_line(arg_file):
    try:
        fd = open(arg_file, 'r')

    except Exception as e:
        raise SystemExit(e)

    file_content = fd.readlines()
    fd.close()

    # The same line had been found.
    same_line_content = []

    source_line_num = 1
    for source_line in file_content:
        same_line_num = []

        target_line_num = 1
        for target_line in file_content:
            if (source_line.strip() == target_line.strip()) \
            and (source_line_num != target_line_num) \
            and (source_line.strip() not in same_line_content) \
            and (source_line.strip()):
                same_line_num.append(target_line_num)

            target_line_num += 1

        if same_line_num:
            print '\nLine ' + str(source_line_num) + ': ' + source_line.strip()
            print '  Same to line:',
            for ln in same_line_num:
                print str(ln) + ' ',

        same_line_content.append(source_line.strip())
        source_line_num += 1


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Arguments Error!')

    fn = sys.argv[1]
    find_same_line(fn)


if __name__ == '__main__':
    main()

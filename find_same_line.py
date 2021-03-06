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

    source_line_index = 0
    source_line_num = source_line_index + 1
    # Read each line.
    for source_line in file_content:
        same_line_num = []

        if source_line.strip() \
        and source_line.strip() not in same_line_content:
            # Compare the rest of lines.
            target_line_num = source_line_num + 1
            for target_line in file_content[source_line_index + 1:]:
                if source_line.strip() == target_line.strip():
                    same_line_num.append(target_line_num)

                target_line_num += 1

        if same_line_num:
            print 'Line ' + str(source_line_num) + ': ' + source_line.strip()
            print 'Same to line:',
            for ln in same_line_num:
                print str(ln),
            print '\n'

            same_line_content.append(source_line.strip())

        source_line_index += 1
        source_line_num += 1


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Arguments Error!')

    fn = sys.argv[1]
    find_same_line(fn)


if __name__ == '__main__':
    main()

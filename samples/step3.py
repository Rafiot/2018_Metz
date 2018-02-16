#!/usr/bin/env python
# -*- coding: utf-8 -*-

# separator : '\n'
# entries: cat data/bview.20030809.1600.txt | grep ORIGINATED | wc -l  => 1351708
# 10 files => ~ 135171 entries/file

import re


def entries_counter(source_file):
    matches = re.findall('ORIGINATED', open(source_file, 'r').read())
    return len(matches)


def file_split(source_file, entries_per_file, output_file='out_', separator='\n'):
    f = open(source_file, 'r')
    counter = 0
    file_number = 0
    out_file = open(output_file + str(file_number) + '.txt', 'w')

    for line in f:
        if line == separator:
            counter += 1
        if counter > entries_per_file:
            out_file.close()
            counter = 0
            file_number += 1
            out_file = open(output_file + str(file_number) + '.txt', 'w')
        else:
            out_file.write(line)

    f.close()


if __name__ == '__main__':
    entries = entries_counter('../data/bview.20030809.1600.txt')
    entries_per_file = entries / 10 + 1
    file_split('../data/bview.20030809.1600.txt', entries_per_file=entries_per_file)

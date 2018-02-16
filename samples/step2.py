#!/usr/bin/env python
# -*- coding: utf-8 -*-

# separator : '\n'
# entries: cat data/bview.20030809.1600.txt | grep ORIGINATED | wc -l  => 1351708
# 10 files => ~ 135171 entries/file


def file_split(source_file, output_file='out_', separator='\n'):
    f = open(source_file, 'r')
    counter = 0
    file_number = 0
    out_file = open(output_file + str(file_number) + '.txt', 'w')

    for line in f:
        if line == separator:
            counter += 1
        if counter > 135171:
            out_file.close()
            counter = 0
            file_number += 1
            out_file = open(output_file + str(file_number) + '.txt', 'w')
        else:
            out_file.write(line)

    f.close()


if __name__ == '__main__':
    file_split('../data/bview.20030809.1600.txt')

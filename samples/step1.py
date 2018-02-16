#!/usr/bin/env python
# -*- coding: utf-8 -*-

# separator : '\n'
# entries: cat data/bview.20030809.1600.txt | grep ORIGINATED | wc -l  => 1351708
# 10 files => ~ 135171 entries/file


f = open('../data/bview.20030809.1600.txt', 'r')

counter = 0

file_number = 0

out_file = open('out_0.txt', 'w')

for line in f:
    if line == '\n':
        counter += 1
    if counter > 135171:
        out_file.close()
        counter = 0
        file_number += 1
        out_file = open('out_' + str(file_number) + '.txt', 'w')
    else:
        out_file.write(line)

f.close()

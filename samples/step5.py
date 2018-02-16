#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import logging
import argparse
import sys


def entries_counter(source_file):
    with open(source_file, 'r') as f:
        matches = re.findall('ORIGINATED', f.read())
    logging.debug('{} entries in the file.'.format(len(matches)))
    return len(matches)


def file_split(source_file, number_of_files, output_file='out', separator='\n'):
    entries_per_file = round(entries_counter(source_file) / number_of_files)
    logging.debug('{} entries per file.'.format(entries_per_file))
    with open(source_file, 'r') as f:
        counter = 0
        file_number = 0
        logging.debug('Opening {}.'.format('{}_{}.txt'.format(output_file, file_number)))
        out_file = open('{}_{}.txt'.format(output_file, file_number), 'w')

        for line in f:
            if line == separator:
                counter += 1
            if counter > entries_per_file:
                out_file.close()
                counter = 0
                file_number += 1
                logging.debug('Opening {}.'.format('{}_{}.txt'.format(output_file, file_number)))
                out_file = open('{}_{}.txt'.format(output_file, file_number), 'w')
            else:
                out_file.write(line)
        out_file.close()  # Forgotten in the other files


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    arg_parser = argparse.ArgumentParser(description='Split a file in smaller files.')
    arg_parser.add_argument('-o', '--original', required=True, help='Path to the original file')
    arg_parser.add_argument('-n', '--number', type=int, required=True, help='Number of files in the output files')
    arg_parser.add_argument('-d', '--destination', default='out', help='Destination file name (format: {destination}_{number}.txt')
    arg_parser.add_argument('-s', '--separator', default='\n', help='Separator in the original file')
    args = arg_parser.parse_args()

    logging.info('Splitting {} in {} files.'.format(args.original, args.number))

    file_split(source_file=args.original, number_of_files=args.number,
               output_file=args.destination, separator=args.separator)

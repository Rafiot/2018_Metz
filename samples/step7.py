#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse
import sys
import os


def file_split(source_file, number_of_files, output_file='out', separator='\n'):
    if not isinstance(separator, bytes):
        separator = separator.encode()
    logging.debug('File size: {}.'.format(os.path.getsize(source_file)))
    chunk_size = round(os.path.getsize(source_file) / number_of_files)
    logging.debug('Chunk size per file: {}.'.format(chunk_size))

    with open(source_file, 'rb') as f:  # Required to open the file as bytes for seek
        file_number = 0
        while True:
            # Jump of "size" from the current place in the file
            to_write = f.read(chunk_size)
            while True:
                rest_of_line = f.readline()
                if rest_of_line and rest_of_line != separator:
                    to_write += rest_of_line
                else:
                    break
            logging.debug('Opening {}.'.format('{}_{}.txt'.format(output_file, file_number)))
            with open('{}_{}.txt'.format(output_file, file_number), 'wb') as new_f:
                new_f.write(to_write)
                file_number += 1
            if not rest_of_line:
                break


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    arg_parser = argparse.ArgumentParser(description='Split a file in smaller files.')
    arg_parser.add_argument('-o', '--original', required=True, help='Path to the original file')
    arg_parser.add_argument('-n', '--number', type=int, required=True, help='Number of files in the output files')
    arg_parser.add_argument('-d', '--destination', default='out', help='Destination file name (format: {destination}_{number}.txt')
    arg_parser.add_argument('-s', '--separator', default='\n', help='Separator in the original file. Note: the separator needs to be alone on a line.')
    args = arg_parser.parse_args()

    logging.info('Splitting {} in {} files.'.format(args.original, args.number))

    file_split(source_file=args.original, number_of_files=args.number,
               output_file=args.destination, separator=args.separator)

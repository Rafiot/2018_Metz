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
        current_position = 0
        while True:
            precedent_position = current_position
            # Jump of "size" from the current place in the file
            f.seek(chunk_size, os.SEEK_CUR)
            s = f.readline()
            while s and s != separator:
                # find the next separator
                s = f.readline()
            # Get the current place
            current_position = f.tell()
            # Copy and write in the new file everything between precedent_position and current_position
            with open(source_file, 'r') as temp:
                temp.seek(precedent_position)
                copy = temp.read(current_position - precedent_position - 1)
            logging.debug('Opening {}.'.format('{}_{}.txt'.format(output_file, file_number)))
            with open('{}_{}.txt'.format(output_file, file_number), 'w') as new_f:
                new_f.write(copy)
                file_number += 1
            if not s:
                break


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

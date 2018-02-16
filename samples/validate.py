#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import hashlib
import glob


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Make sure the splited files are ths asame as the soruce file.')
    arg_parser.add_argument('-o', '--original', required=True, help='Path to the original file')
    arg_parser.add_argument('-d', '--destination', default='out', help='Destination file name (format: {destination}_{number}.txt')
    args = arg_parser.parse_args()

    with open(args.original, 'rb') as f:
        hash_source = hashlib.sha256(f.read()).hexdigest()
    print(hash_source)

    hash_dest = hashlib.sha256()
    concat_files = b''
    first_file = True
    for out_file in sorted(glob.glob('{}_*.txt'.format(args.destination))):
        with open(out_file, 'rb') as f:
            tmp = f.read()
            if first_file:
                concat_files += tmp
                hash_dest.update(tmp)
                first_file = False
            else:
                concat_files += b'\n' + tmp
                hash_dest.update(b'\n' + tmp)
    dest = hash_dest.hexdigest()
    print(dest)
    with open('foo.txt', 'wb') as f:
        f.write(concat_files)

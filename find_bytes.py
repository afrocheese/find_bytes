__author__ = 'charles'

import argparse
import os
import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_bytes(ba, start, end, match_start, match_end, columns):
    hexStr = ''
    for i in range(start, end):
        if i % columns == 0:
            if match_start <= i <= match_end:
                hexStr += bcolors.ENDC
            if i > start:
                hexStr += ' | '
                hexStr += ''.join(map(chr, [x if 32 < x < 127 else ord('.') for x in ba[i:i+columns]]))
            hexStr += format('\n[%08x] ' % i)
            if match_end >= i >= match_start:
                hexStr += bcolors.OKBLUE
        elif i % 2 == 0:
            hexStr += ' '
        if i == match_start:
            hexStr += bcolors.OKBLUE
        if i == match_end:
            hexStr += bcolors.ENDC
        hexStr += format("%0.2x" % ba[i])
    print(hexStr)

def main():
    parser = argparse.ArgumentParser(description='Finds a sequence of bytes in the specified file.')
    parser.add_argument('-r', '--raw-bytes', required=True,
                      help='sequence of bytes to search for (e.g., "\x00\x04"')
    parser.add_argument('-i', '--input', required=True,
                      help='file to search in')
    parser.add_argument('-g', '--toprint', default=32,
                      help='number of surrounding bytes to print (default 32)', type=int)
    parser.add_argument('-c', '--columns', default=16,
                      help='number of octets per line (default 16)', type=int)
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print('Path {} not found.'.format(args.input))
        sys.exit(1)
    if not args.columns % 2 == 0:
        print('Columns must be a multiple of 2.')
        sys.exit(1)

    ba = bytes(args.raw_bytes, 'utf-8')
    regex = re.compile(ba)

    bytes_read = open(args.input, 'rb').read()

    for match in re.finditer(regex, bytes_read):
        start = match.span()[0]
        end = match.span()[1]

        start = max(0, start - args.toprint)
        start -= start % args.columns

        end += args.toprint
        end += args.columns - (end % args.columns)
        end = min(end, len(bytes_read))

        print_bytes(bytes_read, start, end, match.span()[0], match.span()[1], args.columns)


if __name__ == '__main__':
    main()
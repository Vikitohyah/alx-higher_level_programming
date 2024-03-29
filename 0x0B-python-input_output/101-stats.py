#!/usr/bin/python3
"""
log parsing scripts module.
"""


import sys


if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Checks for regexp match in line.'''
        try:
            line = line[:-1]
            words = line.split(" ")
            size[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except Exception as e:
            pass

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File size: {}".format(size[0]))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))
    a = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if a % 10 == 0:
                print_stats()
            a += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

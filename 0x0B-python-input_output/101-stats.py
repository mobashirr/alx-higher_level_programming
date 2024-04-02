#!/usr/bin/python3

'''script for catch certain codes pattern'''


import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))

def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]
        total_size += size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    except (IndexError, ValueError):
        pass
    return total_size, status_codes

def main():
    total_size = 0
    status_codes = {}
    try:
        line_count = 0
        for line in sys.stdin:
            total_size, status_codes = parse_line(line, total_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

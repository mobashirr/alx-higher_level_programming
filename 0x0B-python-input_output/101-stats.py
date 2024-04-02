#!/usr/bin/python3

import sys

metrics = {
    'total_file_size': 0,
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            metrics['total_file_size'] += file_size
            metrics[status_code] += 1
        except Exception as e:
            pass

        if line_count % 10 == 0:
            print("File size: {}".format(metrics['total_file_size']))
            for code in sorted(metrics.keys()):
                if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    print("{}: {}".format(code, metrics[code]))

except KeyboardInterrupt:
    print("File size: {}".format(metrics['total_file_size']))
    for code in sorted(metrics.keys()):
        if code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print("{}: {}".format(code, metrics[code]))

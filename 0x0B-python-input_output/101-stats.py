#!/usr/bin/python3

'''script for catch specfied code pattern from stdin'''


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

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        try:
            ip, _, _, status_code, file_size = line.split()[0], line.split()[8], line.split()[10], line.split()[12], line.split()[13]
            status_code = int(status_code)
            file_size = int(file_size)
            metrics['total_file_size'] += file_size
            metrics[status_code] += 1
        except:
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
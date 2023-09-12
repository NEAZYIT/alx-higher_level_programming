#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous lines (see input format above)
Number of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
If a status code doesn’t appear, don’t print anything for this status code.
Format: <status code>: <number>
Status codes should be printed in ascending order.
"""


import sys
import signal


def print_statistics(total_size, status_codes):
    """
    Print the statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    Handle the keyboard interruption (CTRL + C).
    """
    print_statistics(total_size, status_codes)
    sys.exit(0)


total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        if len(split_line) > 2:
            status_code = split_line[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        total_size += int(split_line[-1])

        if line_count % 10 == 0:
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    print_statistics(total_size, status_codes)
    sys.exit(0)

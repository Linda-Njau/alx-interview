#!/usr/bin/python3
"""Log Parsing Interview Question solution"""
import sys


import re
import signal

total_file_size = 0
status_code_count = {}
line_count = 0

def print_metrics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = re.search(r'(\d{3}) (\d+)$', line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                status_code_count[status_code] = status_code_count.get(status_code, 0) + 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    print_metrics()

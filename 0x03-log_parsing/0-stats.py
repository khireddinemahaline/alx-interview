#!/usr/bin/python3
""" log parsing
    to write a script that reads stdin line by line and computes metrics
    input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
"""
import sys

def parsing_log():
    """parse stdin"""
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    file_size = 0  # total file size
    count = 0  # total number of lines read
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except Exception:
                pass
            try:
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
            except Exception:
                pass
            if count % 10 == 0:
                print("File size: {}".format(file_size))
                for key, value in sorted(status_codes.items()):
                    if value:
                        print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value:
                print("{}: {}".format(key, value))  # print status code
        raise
    
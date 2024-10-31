#!/usr/bin/python3
"""validate utf-8"""


def validUTF8(data):
    """determine if a given data set represents a valid UTF-8 encoding"""
    return all(data[i] >= 0 and data[i] <= 127 for i in range(len(data)))

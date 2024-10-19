#!/usr/bin/python3
"""
return munim number of operation
"""


def minOperations(n: int) -> int:
    """minum operation"""
    operations = 0
    factor = 2
    if n <= 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

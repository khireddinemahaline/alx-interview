#!/usr/bin/python3
"""
Pascal's Triangle Generator

This script generates Pascal's Triangle
up to a specified number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        List[List[int]]: Rows of Pascal's Triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

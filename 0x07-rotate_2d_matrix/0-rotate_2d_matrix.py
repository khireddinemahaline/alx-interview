#!/usr/bin/python3
"""rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = temp
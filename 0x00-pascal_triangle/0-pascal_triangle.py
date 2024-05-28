#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    triangle = [[1], [1, 1]]

    if n <= 0:
        return []
    if n == 1:
        return triangle[0]
    if n == 2:
        return triangle
    if n > 2:
        for i in range(2, n):
            row = []
            for j in range(0, i-1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])
            row.insert(0, 1)
            row.append(1)
            triangle.append(row)
    return triangle

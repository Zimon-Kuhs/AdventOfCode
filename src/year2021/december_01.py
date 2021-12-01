"""
    Solves the 2021-12-01 problem.

    @author Zimon Kuhs
    @date   2021-12-01
"""

import os

#   Ensures ../data/december_01.txt is located.
data_file = os.path.join(os.path.dirname(__file__), "data/december_01.txt")


def solve():
    """
        Solves the problem for December 01.

        @return the solution to the problem.
    """

    with open(data_file, "r", encoding="utf-8") as data:
        depths = [int(depth) for depth in data.readlines()]

    depths = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]

    result = 0
    for i in range(len(depths) - 3):
        result += 1 if sum(depths[i + 1: i + 4]) > sum(depths[i: i + 3]) else 0

    return result

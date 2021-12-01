"""
    Solves the 2021-12-01 problem.

    @author Zimon Kuhs
    @date   2021-12-01
"""

import os


def solve():
    """
        Solves the problem for December 01.

        @return the solution to the problem.
    """

    os.chdir(os.path.dirname(__file__))

    with open("data/december_01.txt", "r", encoding="utf-8") as the_file:
        contents = [int(depth) for depth in the_file.readlines()]

    result = 0
    for i in range(1, len(contents)):
        result += 1 if contents[i] > contents[i - 1] else 0

    return result

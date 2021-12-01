"""
    Solves the 2021-12-01 problem.

    @author Zimon Kuhs
    @date   2021-12-01
"""

example_report = [
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


def solve():
    """
        Solves the problem for December 01.

        @return the solution to the problem.
    """

    result = 0
    for i in range(1, len(example_report)):
        result += 1 if example_report[i] > example_report[i - 1] else 0

    return result

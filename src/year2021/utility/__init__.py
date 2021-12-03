"""
    File management utilities.

    @author Zimon Kuhs
    @date   2021-12-01
"""

from os.path import basename, dirname, join, realpath


def parse_binary(string_list):
    """
        @param string_list  A list of strings, or a string.
        @return             The input converted to binary numbers.
    """

    if not isinstance(string_list, list):
        string_list = [string_list]

    return [int(number, base=2) for number in string_list]


def parse_problem(script):
    """
        @return all lines in a file as a list.
    """

    base = basename(script).split(".")[1]
    path = realpath(join(dirname(__file__), "..", "data", f"{base}.txt"))

    with open(path, "r", encoding="utf-8") as stuff:
        return stuff.read().split("\n")[:-1]

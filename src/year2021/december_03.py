"""
    Solves the 2021-12-03 problem.

    @author Zimon Kuhs
    @date   2021-12-03
    @see    https://adventofcode.com/2021/day/3
"""

from .utility import parse_binary, parse_problem


def most_common_chars(string_list):
    """
        Builds a string from the most common characters in a list of strings, per index.

        @param string_list  The list of strings.
        @return             A string where at every index the character is the most common by index.
    """

    index = 0
    result = []

    while string_list:

        chars = {}
        deleted = []

        for string in string_list:
            if index >= len(string):
                deleted.append(string)
                continue

            char = string[index]

            if char not in chars:
                chars[char] = 0

            chars[char] += 1

        string_list = [element for element in string_list if element not in deleted]
        if not string_list:
            break

        max_amount = -1
        common = ''

        for char, amount in chars.items():
            if amount > max_amount:
                max_amount = amount
                common = char

        result.append(common)
        index += 1

    return "".join(result)


def invert(binary):
    """
        @param binary   The string to invert.
        @return         The input string binary-inverted.
    """

    result = []

    for digit in binary:
        if digit not in ["0", "1"]:
            raise ValueError(f"Invalid digit in string: {digit}")

        result.append("0" if digit == "1" else "1")

    return "".join(result)


def solve():
    """
        Solves the problem for December 03.

        @return the solution to the problem.
    """

    gamma_string = most_common_chars(parse_problem(__name__))
    gamma = int(parse_binary(gamma_string)[0])
    epsilon = int(parse_binary(invert(gamma_string))[0])

    return gamma * epsilon

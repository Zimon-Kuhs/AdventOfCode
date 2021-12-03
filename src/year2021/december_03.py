"""
    Solves the 2021-12-03 problem.

    @author Zimon Kuhs
    @date   2021-12-03
    @see    https://adventofcode.com/2021/day/3
"""

import sys
from .utility import parse_binary, parse_problem


def frequency_map(string_list, index):
    """
        Calculates a frequency mapping for an array of strings.

            TODO:
                - I would really want this bad boy to be a class but this is Python and I'm (~~efficient~~) lazy.

        @param string_list  The array of strings.
        @param index        The string index of the chars to compare.
        @return             A char -> int map describing how many times a character appeared
                            at the specified index in all the strings.
    """

    frequencies = {}
    for string in string_list:
        if index >= len(string):
            continue

        char = string[index]

        if char not in frequencies:
            frequencies[char] = 0

        frequencies[char] += 1

    return frequencies


def most_common(frequency_map, most=True):
    """
        Find the most frequent character in a frequency map.

        @param frequency_map    The frequency map as described by #frequency_map(list, int).
        @param most             If True, the most frequent character is selected, otherwise the least frequent.
    """

    compare = sys.maxsize * (-1 if most else 1)
    result = ''

    for char, amount in frequency_map.items():
        if most and amount > compare:
            compare = amount
            result = char
        elif not most and amount < compare:
            compare = amount
            result = char

    return result


def character_vote(string_list):
    """
        Builds a string from the most common characters in a list of strings, per index.

        @param string_list  The list of strings.
        @return             A string where at every index the character is the most common by index.
    """

    index = 0
    result = []

    while index < max([len(x) for x in string_list]):
        result.append(most_common(frequency_map(string_list, index)))
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

    gamma_string = character_vote(parse_problem(__name__))
    gamma = int(parse_binary(gamma_string)[0])
    epsilon = int(parse_binary(invert(gamma_string))[0])

    return gamma * epsilon

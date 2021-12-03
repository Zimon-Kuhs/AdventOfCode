"""
    Utility functions for collections.

    @author Zimon Kuhs
    @date 2021-12-03
"""

import sys


def column_count(matrix, column=0):
    """
        Calculates the column-wise number of occurences in a matrix.
        <p>
        N.B. will operator on jagged matrices; rows that are not long enough to have an element at the column index
        are simply ignored, since only occurences are relevant.

            TODO:
                - I would really want this bad boy to be a class but this is Python and I'm (~~efficient~~) lazy.

        @param matrix   The array of arrays which elements to check.
        @param column   The column to check.
        @return         A dictionary element -> amount specifying the number of times
                        the elements occured in the column.
    """

    frequencies = {}
    for array in matrix:
        if len(array) < column:
            continue

        element = array[column]

        if element not in frequencies:
            frequencies[element] = 0

        frequencies[element] += 1

    return frequencies


def most_common(frequency_map, most=True, prefer=None):
    """
        Find the most frequent character in a frequency map.

        TODO:
            - Can be generalized.

        @param frequency_map    The frequency map as described by #frequency_map(list, int).
        @param most             If True, the most frequent character is selected, otherwise the least frequent.
        @param prefer           In the case where
    """

    compare = sys.maxsize * (-1 if most else 1)
    result = ''

    #   I have a feeling there's a one-liner here, but can't think of the movie.
    for char, amount in frequency_map.items():

        # I'm well aware this can be done a few magnitudes more readable, but it's hilarious to me that this works.
        if most and amount > compare or \
            not most and amount < compare or\
            amount is compare and result is not prefer and result not in prefer and (char is prefer or char in prefer):

            compare = amount
            result = char

    return result

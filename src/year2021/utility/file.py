"""
    File management utilities.

    @author Zimon Kuhs
    @date   2021-12-01
"""


import os
import sys


def as_lines(file):

    pointer = open(file)
    contents = pointer.readlines()
    pointer.close()
    return contents

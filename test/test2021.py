"""
    Tests the problems for year 2021.

    @author Zimon Kuhs
    @date   2021-12-01
"""

import os
import sys

sys.path.append(os.path.abspath("./src"))

import unittest
import year2021 as year


# pylint: disable=missing-function-docstring
class Test2021(unittest.TestCase):
    """
        Does a bunch of testing.
    """

    def test_december_01(self):
        self.assertEqual(1608, year.december01())

    def test_december_02(self):
        self.assertEqual(1942068080, year.december02())

    def test_december_03(self):
        self.assertEqual(7928162, year.december03())

    def test_december_04(self):
        self.assertEqual(6594, year.december04())

    def test_december_05(self):
        self.assertEqual("TBI", year.december05())

    def test_december_06(self):
        self.assertEqual("TBI", year.december06())

    def test_december_07(self):
        self.assertEqual("TBI", year.december07())

    def test_december_08(self):
        self.assertEqual("TBI", year.december08())

    def test_december_09(self):
        self.assertEqual("TBI", year.december09())

    def test_december_10(self):
        self.assertEqual("TBI", year.december10())

    def test_december_11(self):
        self.assertEqual("TBI", year.december11())

    def test_december_12(self):
        self.assertEqual("TBI", year.december12())

    def test_december_13(self):
        self.assertEqual("TBI", year.december13())

    def test_december_14(self):
        self.assertEqual("TBI", year.december14())

    def test_december_15(self):
        self.assertEqual("TBI", year.december15())

    def test_december_16(self):
        self.assertEqual("TBI", year.december16())

    def test_december_17(self):
        self.assertEqual("TBI", year.december17())

    def test_december_18(self):
        self.assertEqual("TBI", year.december18())

    def test_december_19(self):
        self.assertEqual("TBI", year.december19())

    def test_december_20(self):
        self.assertEqual("TBI", year.december20())

    def test_december_21(self):
        self.assertEqual("TBI", year.december21())

    def test_december_22(self):
        self.assertEqual("TBI", year.december22())

    def test_december_23(self):
        self.assertEqual("TBI", year.december23())

    def test_december_24(self):
        self.assertEqual("TBI", year.december24())

    def test_december_25(self):
        self.assertEqual("TBI", year.december25())


if __name__ == "__main__":
    unittest.main()

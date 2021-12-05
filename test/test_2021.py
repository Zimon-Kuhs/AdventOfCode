"""
    Tests the problems for year 2021.

    @author Zimon Kuhs
    @date   2021-12-01
"""


import os
import sys
import unittest

sys.path.append(os.path.abspath("./src"))

# pylint: disable=import-error, wrong-import-position
# pep8: disable=E402
import year2021 as year     # noqa


# pylint: disable=missing-class-docstring, missing-function-docstring
class Test2021(unittest.TestCase):

    def test_december_01(self):
        self.assertEqual(1608, year.december_01())

    def test_december_02(self):
        self.assertEqual(1942068080, year.december_02())

    def test_december_03(self):
        self.assertEqual(7928162, year.december_03())

    def test_december_04(self):
        self.assertEqual(2745, year.december_04())

    def test_december_05(self):
        self.assertEqual("TBI", year.december_05())

    def test_december_06(self):
        self.assertEqual("TBI", year.december_06())

    def test_december_07(self):
        self.assertEqual("TBI", year.december_07())

    def test_december_08(self):
        self.assertEqual("TBI", year.december_08())

    def test_december_09(self):
        self.assertEqual("TBI", year.december_09())

    def test_december_10(self):
        self.assertEqual("TBI", year.december_10())

    def test_december_11(self):
        self.assertEqual("TBI", year.december_11())

    def test_december_12(self):
        self.assertEqual("TBI", year.december_12())

    def test_december_13(self):
        self.assertEqual("TBI", year.december_13())

    def test_december_14(self):
        self.assertEqual("TBI", year.december_14())

    def test_december_15(self):
        self.assertEqual("TBI", year.december_15())

    def test_december_16(self):
        self.assertEqual("TBI", year.december_16())

    def test_december_17(self):
        self.assertEqual("TBI", year.december_17())

    def test_december_18(self):
        self.assertEqual("TBI", year.december_18())

    def test_december_19(self):
        self.assertEqual("TBI", year.december_19())

    def test_december_20(self):
        self.assertEqual("TBI", year.december_20())

    def test_december_21(self):
        self.assertEqual("TBI", year.december_21())

    def test_december_22(self):
        self.assertEqual("TBI", year.december_22())

    def test_december_23(self):
        self.assertEqual("TBI", year.december_23())

    def test_december_24(self):
        self.assertEqual("TBI", year.december_24())

    def test_december_25(self):
        self.assertEqual("TBI", year.december_25())


if __name__ == "__main__":
    unittest.main()

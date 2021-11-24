"""
    Used to generate the many files I want for this repo.

    @author Zimon Kuhs
    @date   2021-11-24
"""

import os
import sys


class Prefix:
    """
        Utility class representing a prefix and its level.

        @attribute level    The current prefix depth.
        @attribute space    The string to be used as a prefix.
    """

    def __init__(self, space):
        self.level = 0
        self.space = space

    def string(self):
        """
            Retrieve the prefix' current string representation.

            @return The prefix repeated `level` times.
        """

        result = ""
        for _ in range(0, self.level):
            result = f"{self.space}{result}"
        return result

    def adjust(self, adjustment=1):
        """
            Modify the prefix' current level.

            @param adjustment   The adjustment to make.
        """

        self.set_level(self.level + adjustment)

    def set_level(self, level=0):
        """
            Set the prefix current level.

            @param level    The level to set to.
        """

        self.level = level


def as_string(file_path):
    """
        Reads a file as a string.

        @param file_path    Path to the file to read.
        @return             The contents of `file_path` as a string.
    """

    with open(file_path, "r", encoding="utf-8") as text_file:
        return text_file.read()


def dates(start,
          end,
          year=2021,
          target_date=1,
          target_folder="src"):
    """
        Generates a .java-file for each date in December up to the 25th.

        @param start            The starting date, inclusive.
        @param end              The ending date, inclusive.
        @param year             The year in question.
        @param target_date      Blueprint date number.
        @param target_folder    Years' folder.
    """

    if [number for number in [start, end, target_date] if number < 0]:
        raise ValueError("Date parameters must be non-zero positive.")

    directory = f"{target_folder}/year{str(year)}"
    blueprint = as_string(
        f"{directory}/December{target_date:02d}.java"
    )

    for date in range(1, 26):

        the_path = f"{directory}/December{date:02d}.java"
        with open(the_path, "w", encoding="utf-8") as the_file:

            print()
            contents = blueprint.replace(f"0{target_date}", f"{date:02d}")
            the_file.write(contents)


def tests(start,
          end,
          year=2021,
          folder="test",
          package="test"):
    """
        Writes a test-file.

        TODO:
            -   Add prefix to *all* written lines.
            -   The main write loop should be split into functions.

        @param start    The starting date, inclusive.
        @param end      The ending date, inclusive.
        @param year     The year in question.
        @param folder   The folder to write to.
        @param package  Blueprint folder.
    """

    name = f"Test{year}"

    imports = [
        "static org.junit.Assert.assertEquals",
        f"src.year{year}.*",
        "org.junit.Ignore",
        "org.junit.Test",
    ]

    doc_string = [
        f"Tests the problems for year {year}.",
        "",
        "@author Zimon Kuhs",
        f"@date   {year}-12-DD",
    ]

    function = [
        "@Ignore",
        "@Test",
        "public void testDD() {",
        "    assertEquals(\"TBI\", new DecemberDD().solve());",
        "}"
    ]

    pre = Prefix("    ")
    the_path = os.path.abspath(f"{folder}/Test{year}.java")
    print(f"Writing to {the_path}")

    with open(the_path, "x", encoding="utf-8") as the_file:
        if package:
            the_file.write(f"package {package};\n\n")

        for include in imports:
            the_file.write(f"{pre.string()}import {include};\n")
        the_file.write("\n")

        #
        #   Write the docstring.
        #

        if doc_string:
            the_file.write("/**\n")
        for line in doc_string:
            the_file.write(f" *  {line}\n")
        if doc_string:
            the_file.write(" */\n")

        #
        #   Write the class.
        #

        the_file.write(f"public final class {name} {{\n\n")
        pre.adjust(1)

        #
        #   Write the methods.
        #

        for date in range(start, end + 1):
            date_str = f"{date:02d}"

            for line in function:
                rinsed = line.replace("DD", date_str)
                the_file.write(f"{pre.string()}{rinsed}\n")

            the_file.write("\n")

        pre.adjust(-1)
        the_file.write("}\n\n")


if __name__ == "__main__":
    if len(sys.argv) <= 1 or not any(["-f" in sys.argv, "-F" in sys.argv]):
        print("To run this script, you have to enforce it with -f or -F.")
        sys.exit(1)

    dates(1, 25)
    tests(1, 25)

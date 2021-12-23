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


# pylint: disable=too-many-arguments, too-many-locals
def dates(start,
          end,
          year=2021,
          extension="py",
          target_date=1,
          target_folder="src"):
    """
        Generates a .py-file for each date in December up to the 25th.

        @param start            The starting date, inclusive.
        @param end              The ending date, inclusive.
        @param year             The year in question.
        @param extension        The file extension to use.
        @param target_date      Blueprint date number.
        @param target_folder    Years' folder.
    """

    if [number for number in [start, end, target_date] if number < 0]:
        raise ValueError("Date parameters must be non-zero positive.")

    directory = f"{target_folder}/year{str(year)}"
    blueprint = as_string(
        f"{directory}/december_{target_date:02d}.{extension}"
    )

    exports = []
    for date in range(1, 26):

        name = f"december_{date:02d}"
        exports.append(name)

        the_file = f"{directory}/{name}.{extension}"

        print(f"Writing to {the_file}")
        with open(the_file, "w", encoding="utf-8") as source_file:

            contents = blueprint.replace(f"0{target_date}", f"{date:02d}")
            source_file.write(contents)
        print()

    print(f"Writing to {directory}/__init__.py")
    with open(f"{directory}/__init__.py", "w", encoding="utf-8") as init:
        for export in exports:
            init.write(f"from .{export} import solve as {export}\n")
    print()


# pylint: disable=too-many-arguments, too-many-locals
def tests(start,
          end,
          year=2021,
          extension="py",
          folder="test"):
    """
        Writes a test-file.

        TODO:
            -   Add prefix to *all* written lines.
            -   The main write loop should be split into functions.

        @param start        The starting date, inclusive.
        @param end          The ending date, inclusive.
        @param year         The year in question.
        @param extension    The file extension to use.
        @param folder       The folder to write to.
    """

    name = f"Test{year}"

    imports = [
        "unittest",
        f"year{year} as year",
    ]

    doc_string = [
        f"Tests the problems for year {year}.",
        "",
        "@author Zimon Kuhs",
        f"@date   {year}-12-01",
    ]

    function = [
        "def test_december_DD(self):",
        "    self.assertEqual(\"TBI\", year.december_DD())",
    ]

    the_main = [
        "if __name__ == \"__main__\":",
        "    unittest.main()"
    ]

    pre = Prefix("    ")
    the_path = os.path.abspath(f"{folder}/test_{year}.{extension}")

    print(f"Writing to {the_path}")
    with open(the_path, "w", encoding="utf-8") as the_file:
        #
        #   Write the docstring.
        #

        if doc_string:
            comment_guard = "\"\"\"\n"
            the_file.write(comment_guard)

            for line in doc_string:
                the_file.write(f"    {line}\n")

            the_file.write(f"{comment_guard}\n")

        #
        #   Write the imports.
        #

        the_file.write("import os\nimport sys\n\nsys.path.append(os.path.abspath(\"./src\"))\n\n")
        for include in imports:
            the_file.write(f"{pre.string()}import {include}\n")

        the_file.write("\n")

        #
        #   Write the class.
        #

        the_file.write(f"class {name}(unittest.TestCase):\n\n")
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
        the_file.write("\n")

        for line in the_main:
            the_file.write(f"{line}\n")


def generate_c_files(
        start,
        end,
        input_path,
        output_folder,
        year=2015):

    lines = as_string(input_path).split("\n")

    with open(f"{output_folder}/year{year}.h", "w", encoding="utf-8") as the_file:
        the_file.write(f"#ifndef __YEAR_{year}__\n")
        the_file.write(f"#define __YEAR_{year}__\n\n")

        for date in range(start, end + 1):
            the_file.write(f"int december{date:02d}();\n")

        the_file.write(f"\n#endif  // __YEAR_{year}__\n")

    for date in range(start, end + 1):
        with open(f"{output_folder}/december{date:02d}.c", "w", encoding="utf-8") as the_file:
            for line in lines:
                the_file.write(line.replace("DD", f"{date:02d}") + "\n")


def generate_c_tests(start,
                     end,
                     input_path,
                     output_path="test",
                     year=2015):

    lines = [
        "START_TEST (test_DD) {",
        "",
        "fail_unless(decemberDD() == 0, \"December DD failed.\");",
        "",
        "} END_TEST"
    ]

    output = []
    for line in as_string(input_path).split("\n"):
        if line == "#define TESTS_HERE":

            output.append(f"#include \"year{year}.h\"\n")

            for date in range(start, end + 1):
                for test_line in lines:
                    output.append(test_line.replace("DD", f"{date:02d}"))
                output.append("")

        elif line == "#define TEST_CASES_HERE":
            for date in range(start, end + 1):
                output.append(f"    tcase_add_test(tc1_1, test_{date:02d});")

        else:
            output.append(line)

    with open(f"{output_path}/test{year}.c", "w", encoding="utf-8") as the_file:
        for line in output:
            the_file.write(line + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] != "-f" and sys.argv[2] != "-F":
        print("To run this script, you have to enforce it with -f or -F.")
        sys.exit(1)

    parsed = int(sys.argv[1])

    generate_c_tests(1, 25, "dev/c/tests.c", output_path="test")
    generate_c_files(1, 25, "dev/c/problem.c", f"src/year{parsed}", parsed)

    # dates(1, 25, year)
    # tests(1, 25, year)

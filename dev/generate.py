"""
    Used to generate the many files I want for this repo.

    @author Zimon Kuhs
    @date   2021-11-24
"""

import sys


def EXTENSION_MAP():
    """
        Constant.
    """

    return {
        2015: "c",
        2016: "cpp",
        2017: "hs",
        2018: "r",
        2019: "cs",
        2020: "scala",
        2021: "py"
    }


def GENERATOR_MAP():
    """
        Constant.
    """

    return {
        2015: generateC,
        2016: generateCPP,
        2017: generateHaskell,
        2018: generateR,
        2019: generateCS,
        2020: generateScala,
        2021: generatePython
    }


def asLines(target):
    """
        Reads a file's lines into an array.

        @param target   Path to the file to read.
        @return         The contents of `file_path` as an array of lines.
    """

    with open(target, "r", encoding="utf-8") as theFile:
        return theFile.read().split("\n")


def includes(statement, imports):
    """
        Generates a list of include/import statements.

        @param statement    The statement.
        @param imports      List of things to include/import/et.c.
        @return             A list of statement strings.
    """

    return [f"{statement} {identifier}" if len(identifier) > 0 else "" for identifier in imports]


def docString(year, guard, prefix):
    """
        Generates a docstring for a file.

        @param year     The year to put in the docstring.
        @param guard    The block comment prefix and postfix guard. If list, split into pre- and post-.
        @param prefix   Prefix to use in front
        @return         A generated docstring as a list of string lines.
    """

    preGuard = postGuard = guard
    if isinstance(guard, list):
        preGuard = guard[0]
        postGuard = guard[1]

    return [
        preGuard,
        f"{prefix}Tests the problems for year {year}.",
        f"{prefix}",
        f"{prefix}@author Zimon Kuhs",
        f"{prefix}@date   {year}-12-01",
        postGuard,
    ]


def generateSolutions(year, blueprint, output):
    """
        Generates solution files.

        @param string   The base string.
        @param year     The year to insert on "YYYY"
        @return         Copy of the base string with numbers inserted over time-stamp placeholders.
    """

    lines = asLines(blueprint)

    for date in range(1, 26):
        with open(f"{output}/year{year}/december{date:02d}.{EXTENSION_MAP()[year]}", "w", encoding="utf-8") as the_file:
            for line in lines:
                the_file.write(insertTime(line, year, date) + "\n")


def insertTime(string, year, date):
    """
        Replaces time-stamp placeholders with actual numbers.

        @param string   The base string.
        @param year     The year to insert on "YYYY"
        @param date     The date to insert on "DD"
        @return         Copy of the base string with numbers inserted over time-stamp placeholders.
    """

    return string.replace("DD", f"{date:02d}").replace("YYYY", f"{year}")


def generateC(year, blueprint, source, test):
    """
        Generate C files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    # # # # # # # # # # # # # # # # # # # # #   Tester file generation.    # # # # # # # # # # # # # # # # # # # # #

    lines = includes("#include", ["<check.h>", "", f"\"year{year}.h\""])
    lines.append("")

    testLines = [
        "START_TEST (test_DD) {\n",
        "    fail_unless(decemberDD() == 0, \"December DD failed.\");\n",
        "} END_TEST"
    ]

    for date in range(1, 26):
        for line in testLines:
            lines.append(insertTime(line, year, date))
        lines.append("")

    lines.append("int main(void) {\n")
    lines.append("    Suite *suite = suite_create(\"Core\");")
    lines.append("    TCase *testCore = tcase_create(\"Core\");")
    lines.append("    SRunner *suiteRunner = srunner_create(suite);")
    lines.append("    int numberFailed;\n")
    lines.append("    suite_add_tcase(suite, testCore);")

    for date in range(1, 26):
        lines.append(insertTime("    tcase_add_test(testCore, test_DD);", year, date))

    lines.append("\n    srunner_run_all(suiteRunner, CK_ENV);")
    lines.append("    numberFailed = srunner_ntests_failed(suiteRunner);")
    lines.append("    srunner_free(suiteRunner);\n")

    lines.append("    return numberFailed & 1;")
    lines.append("}\n")

    with open(f"{test}/test{year}.c", "w", encoding="utf-8") as output:
        for line in lines:
            output.write(line + "\n")

    # # # # # # # # # # # # # # # # # # # # #   Header file generation.    # # # # # # # # # # # # # # # # # # # # #

    with open(f"{source}/year{year}/year{year}.h", "w", encoding="utf-8") as output:
        headerGuard = f"__YEAR_{year}_H__"
        output.write(f"#ifndef {headerGuard}\n")
        output.write(f"#define {headerGuard}\n\n")

        for date in range(1, 26):
            output.write(f"int december{date:02d}();\n")

        output.write(f"\n#endif  // {headerGuard}\n")

    # # # # # # # # # # # # # # # # # # # # #   Source file generation.    # # # # # # # # # # # # # # # # # # # # #

    generateSolutions(year, blueprint, source)


def generateCPP(blueprint, source, test):
    """
        Generate C++ files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    raise NotImplementedError("2016")


def generateHaskell(blueprint, source, test):
    """
        Generate Haskell files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    raise NotImplementedError("2017")


def generateR(blueprint, source, test):
    """
        Generate R files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    raise NotImplementedError("2018")


def generateCS(blueprint, source, test):
    """
        Generate C# files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    raise NotImplementedError("2019")


def generateScala(blueprint, source, test):
    """
        Generate Scala files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    raise NotImplementedError("2020")


def generatePython(year, blueprint, source, test):
    """
        Generate Python files.

        @param year         The year for which to generate.
        @param blueprint    Blueprint file for problems.
        @param source       The output directory for solution files.
        @param test         The output directory for the tester file.
    """

    # # # # # # # # # # # # # # # # # # # # #   Tester file generation.    # # # # # # # # # # # # # # # # # # # # #

    lines = docString(year, "\"\"\"", "    ")
    lines.append("")

    for line in includes("import", ["os", "sys"]):
        lines.append(line)
    lines.append("\nsys.path.append(os.path.abspath(\"./src\"))\n")

    for line in includes("import", ["unittest", f"year{year} as year", ""]):
        lines.append(line)

    lines.append("\n# pylint: disable=missing-function-docstring")
    lines.append(f"class Test{year}(unittest.TestCase):")
    lines.append("    \"\"\"\n        Does a bunch of testing.\n    \"\"\"\n")

    for date in range(1, 26):
        lines.append(insertTime(
            "    def test_december_DD(self):\n        self.assertEqual(\"TBI\", year.decemberDD())\n",
            year, date))

    lines.append("\nif __name__ == \"__main__\":\n    unittest.main()")

    with open(f"{test}/test{year}.py", "w", encoding="utf-8") as the_file:
        for line in lines:
            the_file.write(line + "\n")

    # # # # # # # # # # # # # # # # # # # #   __init__.py file generation.    # # # # # # # # # # # # # # # # # # # #

    with open(f"{source}/year{year}/__init__.py", "w", encoding="utf-8") as init:
        for date in range(1, 26):
            name = insertTime("decemberDD", year, date)
            init.write(f"from .{name} import solve as {name}\n")

    # # # # # # # # # # # # # # # # # # # # #   Source file generation.    # # # # # # # # # # # # # # # # # # # # #

    generateSolutions(year, blueprint, source)


if __name__ == "__main__":
    """
        TODO:
            - Take paths as arguments.
    """

    if len(sys.argv) != 3 or sys.argv[2] != "-f" and sys.argv[2] != "-F":
        print("To run this script, you have to enforce it with -f or -F.")
        sys.exit(1)

    inputYear = int(sys.argv[1])

    if inputYear not in GENERATOR_MAP():
        raise ValueError(f"Year {inputYear} is not supported and probably won't be until it hits.")

    extension = EXTENSION_MAP()[inputYear]
    blueprintDirectory = f"dev/blueprints/{extension}/blueprint.{extension}"
    sourceDirectory = "src"
    testDirectory = "test"

    GENERATOR_MAP()[inputYear](inputYear, blueprintDirectory, sourceDirectory, testDirectory)

"""
    Solves the 2021-12-04 problem.

    @author Zimon Kuhs
    @date   2021-12-05
    @see    https://adventofcode.com/2021/day/4
"""


from .utility import Board, parse_problem, ParseError


def find_winner(boards, draws):
    """
        Find the winner of a bingo game.

        @param boards   The boards in play.
        @param draws    The list of drawn numbers, in order.
        @return         The board score (last drawn number multiplied by the sum of non-checked numbers in the board).
        @see            .utility.Board
    """

    for draw in draws:
        for board in boards:
            if board.check(draw):
                return draw * board.sum_unchecked()
    return -1


def solve():
    """
        Solves the problem for December 04.

        @return the solution to the problem.
    """


    lines = parse_problem(__name__)
    draws = [int(number) for number in lines.pop(0).split(",")]

    boards = []
    while len(lines) >= 5:
        boardLines, lines = lines[1:6], lines[6:]
        boards.append(Board(boardLines))

    if len(lines):
        raise ParseError(f"{len(lines)} lines left!")

    return find_winner(boards, draws)

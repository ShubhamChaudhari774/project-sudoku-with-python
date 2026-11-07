
import sys
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class ClingoApp(Application):

    def print_model(self, model, printer):
        board = Sudoku.from_model(model)
        print(board)
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()


if __name__ == "__main__":
    clingo_main(ClingoApp())

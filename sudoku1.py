import sys
from clingo.application import Application, clingo_main


class ClingoApp(Application):
    def print_model(self, model, printer):
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
        sys.stdout.flush()

    
    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()


if __name__ == "__main__":
    clingo_main(ClingoApp())
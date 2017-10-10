import chess.pgn
import chess.svg
import time
from IPython.display import SVG, display


def render_svg(board, size):
    display(SVG(chess.svg.board(board=board,
                                lastmove=board.peek(),
                                size=size)))


def save_pgn(board, name):
    handle = open(name + ".pgn", "w")
    game = chess.pgn.Game().from_board(board)
    game.headers["Event"] = "AI"
    game.headers["Site"] = "???"
    game.headers["Date"] = time.strftime("%Y.%m.%d")
    game.headers["White"] = "Agent #1"
    game.headers["Black"] = "Agent #2"
    game.headers["Result"] = board.result()
    print(game, file=handle)
    handle.close()

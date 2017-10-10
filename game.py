import chess

board = chess.Board()
move = chess.Move(chess.E2, chess.E3)
board.push(move)

m1w = chess.Move(chess.E2, chess.E3)
board.push(m1w)
m1b = chess.Move(chess.C7, chess.C6)
board.push(m1b)
m2w = chess.Move(chess.F1, chess.C4)
board.push(m2w)
m2b = chess.Move(chess.G8, chess.H6)
board.push(m2b)

for move in board.legal_moves:
    print(move.uci())

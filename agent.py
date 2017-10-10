import chess


class Agent:
    def __init__(self, color):
        self.color = color

    def best_move(self, board):
        best_move = chess.Move.null()
        best_reward = 0
        for move in board.legal_moves:
            reward = self.position_reward(board, move)
            print(move)
            print(reward)
            print("\n")
            if reward > best_reward:
                best_reward = reward
                best_move = move
        return best_move

    def position_reward(self, board, move):
        reward = 0
        for attack in board.attacks(move.to_square):
            print("attacks: ")
            print(attack)
            reward += 1
        for attacker in board.attackers(not self.color, move.to_square):
            print("attacker: ")
            print(attacker)
            reward -= 1
        return reward

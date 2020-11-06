# create parent class that stores scrabble scores
class Scrabble
    def __init__(self):
        self.scrab_dict = {
            1: [A, E, I, O, U, L, N, R, S, T],
            2: [D, G],
            3: [B, C, M, P],
            4: [F, H, V, W, Y],
            5: [K],
            8: [J, X],
            10: [Q, Z]
        }

    def score(self):

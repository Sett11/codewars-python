from collections import namedtuple
from operator import mul

Game = namedtuple("Game", ["name", "outcomes"])

def find_best_game(a):
    return max([[sum(mul(*j) for j in i.outcomes),i.name] for i in a])[1]

g1 = Game("Breakeven Steven", ((0.5, 20), (0.5, -20)))

# EV = -0.1
g2 = Game("Go big or go home", ((0.99, -10), (0.01, 980)))

# EV = -0.2
g3 = Game("Steady Eddy", ((0.51, -10), (0.49, 10)))

# EV = -20
g4 = Game("The staircase", ((0.75, -100), (0.10, 100),
                            (0.05, 200),(0.05, 300),
                            (0.05, 400)))

print(find_best_game((g1,g2,g3,g4)))
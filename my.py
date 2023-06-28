def covered_pawns(p):
    a,b=[[['a1', 0, 0], ['a2', 1, 0], ['a3', 2, 0], ['a4', 3, 0], ['a5', 4, 0], ['a6', 5, 0], ['a7', 6, 0], ['a8', 7, 0]], [['b1', 0, 1], ['b2', 1, 1], ['b3', 2, 1], ['b4', 3, 1], ['b5', 4, 1], ['b6', 5, 1], ['b7', 6, 1], ['b8', 7, 1]], [['c1', 0, 2], ['c2', 1, 2], ['c3', 2, 2], ['c4', 3, 2], ['c5', 4, 2], ['c6', 5, 2], ['c7', 6, 2], ['c8', 7, 2]], [['d1', 0, 3], ['d2', 1, 3], ['d3', 2, 3], ['d4', 3, 3], ['d5', 4, 3], ['d6', 5, 3], ['d7', 6, 3], ['d8', 7, 3]], [['e1', 0, 4], ['e2', 1, 4], ['e3', 2, 4], ['e4', 3, 4], ['e5', 4, 4], ['e6', 5, 4], ['e7', 6, 4], ['e8', 7, 4]], [['f1', 0, 5], ['f2', 1, 5], ['f3', 2, 5], ['f4', 3, 5], ['f5', 4, 5], ['f6', 5, 5], ['f7', 6, 5], ['f8', 7, 5]], [['g1', 0, 6], ['g2', 1, 6], ['g3', 2, 6], ['g4', 3, 6], ['g5', 4, 6], ['g6', 5, 6], ['g7', 6, 6], ['g8', 7, 6]], [['h1', 0, 7], ['h2', 1, 7], ['h3', 2, 7], ['h4', 3, 7], ['h5', 4, 7], ['h6', 5, 7], ['h7', 6, 7], ['h8', 7, 7]]],[]
    [b.extend(i) for i in a]
    c=[i[1:] for i in b if i[0] in p]
    return len([i for i in c if [i[0]-1,i[1]-1] in c or [i[0]-1,i[1]+1] in c])

print(covered_pawns(['e5', 'b2', 'b4', 'g4', 'a1', 'a5']))
print(covered_pawns(['a2', 'b1',"c2"]))
print(covered_pawns(['f7', 'b1', 'h1', 'c7', 'h7']))
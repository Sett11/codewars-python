def game(a):
    if not a or not a[0]:
        return []
    for i in range(len(a)-1):
        if not a[i+1] or a[i][-1]!=a[i+1][0]:
            return a[:i+1]
    return a

print(game(["dog","goose","elephant","tiger","rhino","orc","cat"]))
print(game(["dog","goose","elephant","higer","rhino","orc","cat"]))
print(game(["dog","goose","","higer","rhino","orc","cat"]))
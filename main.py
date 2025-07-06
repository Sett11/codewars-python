def find_variable():
    g = globals()
    return [i for i in g if g[i] == 777][0]
def whoseMove(l,w):
    return l if w else [i for i in ['black','white'] if i!=l][0]

print(whoseMove('black',False))
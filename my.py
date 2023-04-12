def f(e,alf='abcdefghijklmnopqrstuvwxyz'):
    return alf.index(e)+1

def add_letters(*letters):
    alf='abcdefghijklmnopqrstuvwxyz'
    if(letters=='z' or len(letters)==0):return 'z'
    g=sum(list(map(f,letters)))
    g=g%len(alf)
    return alf[g-1]

print(add_letters('y', 'c', 'b'))
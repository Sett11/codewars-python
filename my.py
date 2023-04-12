def f(e):
    return e.find('O')!=-1

def car_crash(r):
    if(r.find('O')==-1):return False
    r=r.split('\n')
    r=list(filter(f,r))
    r=''.join(r)
    g=r.find('O')
    return r.find('X',g)!=-1

print(car_crash("""
                      X
            X   O='`o
                      X   """.strip()))
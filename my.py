def turn(c,t):
    a=['N','E','S','W']
    r,l='right','left'
    return l if [c,t]==[a[0],a[-1]] else r if [c,t]==[a[-1],a[0]] else r if a.index(c)<a.index(t) else l


print(turn('S','E'))
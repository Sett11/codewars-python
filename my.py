def is_kiss(w):
    w=list(map(len,w.split()))
    return 'Good work Joe!' if len(w)>=max(w) else 'Keep It Simple Stupid'

print(is_kiss('Joe had a bad day'))
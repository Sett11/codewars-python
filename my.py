from bisect import insort

def sort(s):
    r=[]
    for i in s:
        insort(r,i)
    return iter(r)
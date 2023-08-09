from functools import reduce as r
def check_root(s):
    a=s.replace('-','').split(',')
    if len(a)!=4 or len([i for i in a if not i.isdigit()]):
        return 'incorrect input'
    if not all([abs(int(a[i+1])-int(a[i]))==1 for i in range(len(a)-1)]):
      return 'not consecutive'
    q=r(lambda e,u:e*u,[int(i) for i in a])+1
    return f'{q}, {int(q**.5)}'

print(check_root('-4,-3,-2,-1'))
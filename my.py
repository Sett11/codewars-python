def count_arara(n,s=''):
    while n>1:
        s+='adak ';n-=2
    return s + 'anane' if n==1 else s.rstrip()

print(count_arara(13))
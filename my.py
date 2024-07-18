# def f(n):
#     t=sum(i*(i+1)//2 for i in range(1,n+1))
#     return t*(t+1)//2

# d={i:f(i) for i in range(10**9+1)}

# def sum_of_sums(n):
#     a=[f(i) for i in range(1,13)]
#     b=[a[i+1]-a[i] for i in range(len(a)-1)]
#     x,y=1,2
#     return 

# print(sum_of_sums(100))

def deemojify(s):
    d={':)':'0',':D':'1','>(':'2','>:C':'3',':/':'4',':|':'5',':O':'6',';)':'7','^.^':'8',':(':'9'}
    return ''.join(chr(int(''.join(d[j] for j in i.split()))) for i in s.split('  '))

print(deemojify(':D :) :/  :D :) :|'))
def sequence_sum(a,b,c):
    n=(b-a)//c
    return 0 if n<0 else (n+1)*(n*c+(a*2))//2

print(sequence_sum(780, 6851543, 5))
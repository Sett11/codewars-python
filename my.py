def frog_contest(n):
    a=n*(n+1)//2
    b=a//2
    c=b*(b+1)//2
    return f"Chris ate {a} flies, Tom ate {c} flies and Cat ate {(a+c)*(a+c+1)//2} flies"

print(frog_contest(8))
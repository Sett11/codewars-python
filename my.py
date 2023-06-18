from functools import reduce as r
def main_diagonal_product(m):
    return r(lambda a,c:a*c[0],[[i for k,i in enumerate(h) if k==n] for n,h in enumerate(m)],1)

print(main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]))
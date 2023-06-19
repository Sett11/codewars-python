from functools import reduce as r
def smallest_product(a):
    return min([r(lambda a,c:a*c,i,1) for i in a])

print(smallest_product([[3, 2], [1, 2, 1], [7, 8]]))
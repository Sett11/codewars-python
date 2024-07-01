def is_triangle_number(n):
    if isinstance(n,int) and not isinstance(n,bool):
        x=(8*n+1)**.5
        return int(x)==x
    return False
    
print(is_triangle_number(2098176))    
print(is_triangle_number(949941))    
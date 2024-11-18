def get_w(h):
    if h<2:
        return []
    a=[(' '*(h-i-1)+'*'+' '*(i*2-1)+'*'+' '*(h-i-1)).replace('**','*') for i in range(h-1,-1,-1)]
    return [i+j[1:] for i,j in zip(a,a)]

print(*get_w(22),sep='\n')
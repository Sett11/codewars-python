def print_nums(*a):
    b=[*a];m=len(str(max(b,default=0)))
    return '\n'.join(list(map(lambda e:'0'*(m-len(str(e)))+str(e),b)))

print(print_nums(1009, 2))
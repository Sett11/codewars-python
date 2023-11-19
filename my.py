def pattern(n):
    if n<1:
        return ''
    return '\n'.join([''.join([str(i)]*i) for i in range(2,n+1,2)])


print(pattern(6))
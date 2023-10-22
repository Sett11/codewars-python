def is_pronic(n):
    for i in range(1,n+1):
        if i*(i+1)==n:
            return True
    return not bool(n)

print(is_pronic(30))
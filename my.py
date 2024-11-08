def strongest_even(n,m):
    return n if m-n<1 else n+(n%2) if m-n<2 else 2*strongest_even((n+(n%2))//2,(m-(m%2))//2)

print(strongest_even(129,193))
def square_up(n):
    return sum([sum([[0]*j]+[[i for i in range(n,0,-1)][j:]],[]) for j in range(n)][::-1],[])

print(square_up(4))
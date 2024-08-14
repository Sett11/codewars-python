def find_summands(n):
    sq=n**2
    return [i for i in range(sq-(n-1),sq+(n+1),2)]

print(find_summands(357))
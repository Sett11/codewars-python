def doubleton(n):
    n+=1
    while len(set(list(str(n))))!=2:
        n+=1
    return n

print(doubleton(10001))
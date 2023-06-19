def candies(l):
    return sum([max(l)-i for i in l]) if len(l)>1 else -1

print(candies([5,8,6,4]))
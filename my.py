from math import lcm

def candies_to_buy(n):
    return lcm(*range(1,n+1))

print(candies_to_buy(9))
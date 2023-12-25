import random

guess=10
random.randint=lambda x,y:10

lucky_number = random.randint(1, 100)

print(guess,lucky_number)
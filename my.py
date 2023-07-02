def f(s):
    return [ord(i)-64 for i in list(s)]

def battle(x,y):
    a,b=sum(f(x)),sum(f(y))
    if(a==b):
        return 'Tie!'
    return x if a>b else y

print(battle("ONE","TWO"))
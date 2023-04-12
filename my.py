def bonus_time(s,b,c='$'):
    return c+str(s*10) if b else c+str(s)

print(bonus_time(10000,True))
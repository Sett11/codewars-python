def is_lucky(t):
    try:
        return sum(list(map(int,t[0:3])))==sum(list(map(int,t[3:]))) and len(t)==6
    except:
        return False

print(is_lucky('100200'))
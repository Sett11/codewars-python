def generator (f,t,s):
    if not s:
        return []
    return [i for i in range(f,t+1 if f<t else t-1,s if f<t else -s)]

print(generator(20,10,1))
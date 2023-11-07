def lstzip(a,b,fn):
    return [fn(*i) for i in zip(a,b)]

print(lstzip([1, 2, 3, 4, 5],['a', 'b'],lambda a,b: str(a)+str(b)))
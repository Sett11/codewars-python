def highest_value(a,b):
    f=lambda x:sum(ord(i) for i in x)
    return [b,a][f(a)>=f(b)]

print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))
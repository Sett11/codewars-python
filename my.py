def flatten_me(a):
    r=[]
    for i in a:
        if type(i) is list:
            for j in i:
                r.append(j)
        else:
            r.append(i)
    return r

print(flatten_me([[True, False], ['!'], ['?'], [71, '@']]))
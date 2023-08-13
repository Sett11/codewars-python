def to_query_string(o):
    a=[]
    for i in o:
        if type(o[i])!=list:
            a.append(f'{i}={o[i]}')
        else:
            j=0
            while j<len(o[i]):
                a.append(f'{i}={o[i][j]}')
                j+=1
    return '&'.join(a)

print(to_query_string({"bar": [2, 4], "foo": [1, 3]}))
print(to_query_string({ "bar": 2, "foo": 1 }))
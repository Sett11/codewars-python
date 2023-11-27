def process_2arrays(a,b):
    a,b=set(a),set(b)
    l,t,p=len(a&b),len(a^b),len(a-b)
    return [l,t,p,t-p]

print(process_2arrays([33, 2, 3, 37, 38, 40, 12, 10, 43, 44, 47, 49, 8, 19, 22, 24, 26, 28, 29, 30],[1, 34, 17, 7, 9, 10, 43, 49, 22, 27, 28]))
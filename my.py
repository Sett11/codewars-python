def repeat_sequence_len(n):
    r=[]
    while True:
        if n in r:
            return len(r)-r.index(n)
        r.append(n)
        n=sum([int(i)**2 for i in str(n)])


print(repeat_sequence_len(818))
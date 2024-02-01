def name_file(a,b,c):
    r=[]
    while len(r)<b and all(isinstance(i,int) for i in [b,c]):
        r.append(a.replace('<index_no>',str(c)))
        c+=1
    return r

print(name_file('<file> number <index_no>', 5, 0))
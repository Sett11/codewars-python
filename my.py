def get_cell_addresses(r):
    t=[[i[0],i[1:]] for i in r.replace('Range ','').split(':')]
    a,b,c,d=ord(t[0][0])-65,int(t[0][1]),ord(t[1][0])-65,int(t[1][1])
    r=sum([[chr(i+65)+str(j) for i in range(a,c+1)] for j in range(b,d+1)],[])
    return r if len(r)>1 else []

print(get_cell_addresses("Range B3:D5"))
print(get_cell_addresses("Range F12:J17"))
print(get_cell_addresses("Range H7:H7"))
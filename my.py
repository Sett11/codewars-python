def ulam_sequence(a,b,n):
    sq=[0]*1000000
    r=[a,b]
    sq[a+b]=1
    i=a+b
    while len(r)<n:
      if sq[i]==1:
        for x in r:
          sq[x+i]+=1
        r.append(i)
      i+=1
    return r

print(ulam_sequence(2,5,300))
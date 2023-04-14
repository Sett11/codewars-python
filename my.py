def redistribute_wealth(a):
    b=sum(a)/len(a);l=len(a);i=0
    a.clear()
    while i<l:
        a.append(b)
        i+=1

print(redistribute_wealth([2,2,3]))
def sorted_comm_by_digs(a,b):
    dr,dsddr=lambda x:sum(map(int,str(x))),lambda x:sum(map(lambda y:int(y)**2,str(x)))
    return sorted(set(a)&set(b),key=lambda x:(-(dsddr(k:=dr(x))+k),x))

print(sorted_comm_by_digs([5, 56, 28, 35, 12, 27, 64, 99, 18, 31, 14, 6],[28, 17, 31, 63, 64, 5, 18, 17, 95, 56, 37, 5, 28, 16]))
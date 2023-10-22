def work_needed(n,f):
    k=n-sum([i[0]*60+i[1] for i in f])
    return "Easy Money!" if k<1 else f"I need to work {(k)//60} hour(s) and {(k)%60} minute(s)"


print(work_needed(141, [(1,55), (0,25)]))
print(work_needed(60, [(1,0)]))
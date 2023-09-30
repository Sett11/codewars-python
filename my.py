def empty_values(a):
    for i in range(len(a)):
        if type(a[i])==int:
            a[i]=0
        elif type(a[i])==float:
            a[i]=0.0
        elif type(a[i])==str:
            a[i]=''
        elif type(a[i])==list:
            a[i]=[]
        elif type(a[i])==dict:
            a[i]={}
        elif type(a[i])==tuple:
            a[i]=()
        elif type(a[i])==set:
            a[i]=set()
        elif type(a[i])==bool:
            a[i]=False
        elif type(a[i])=='NoneType':
            a[i]=None
    return a

print(empty_values([7, 3.14, "cat",[1,2],{1:2},(1,2,3),set([1,2,3]),None,True]))
def add2(n):
    return n + 2
def mul7(n):
    return n * 7

def operation_arguments(a):
    i=0
    while i<len(a):
        if not isinstance(a[i],int) and not i:
            a[i]=a[i](0)
        elif not isinstance(a[i],int):
            a[i-1]=a[i](a[i-1])
            a.pop(i)
            i-=1
        i+=1
    return a

print(operation_arguments([1, add2, 5, add2, mul7, 4, mul7]))
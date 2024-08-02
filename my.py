def count_paths(n,c):
    a=[([0]*n)[c[1]:] for _ in range(n)][:c[0]+1]
    for i in range(1,len(a)):
        a[i][0]=1
        for j in range(1,len(a[0])):
            if i==1:
                a[0][j]=1
            a[i][j]=a[i-1][j]+a[i][j-1]
    return 0 if n==1 else a[-1][-1] or 1

print(count_paths(21,(16,0)),sep='\n')
print(count_paths(44,(13,10)),sep='\n')

# class LazyInit(type):
#      def __init__(cls,name,bases,dct):
#           print(list(locals().items()))
#           super().__init__(name,bases,dct)

# class MyClass(metaclass=LazyInit):
#      def __init__(self,name,age):
#           pass
     
# m=MyClass('John',23)
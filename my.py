def count_cash(a,c):
    n,r,u=len(a),[],set()
    def dfs(i,j,k):
        if i<0 or j<0 or j>=n or (i,j) in u:
            return
        k+=a[i][j]
        if [i,j]==[0,n-1]:
            r.append(k)
            return
        dfs(i-1,j,k)
        dfs(i,j+1,k)
    dfs(c[0],c[1],0)
    return max(r)

print(count_cash([[3, 3, -1],[-1, 5, -2],[4, -2, 6]],(1,0)),sep='\n')

# class LazyInit(type):
#      def __init__(cls,name,bases,dct):
#           print(list(locals().items()))
#           super().__init__(name,bases,dct)

# class MyClass(metaclass=LazyInit):
#      def __init__(self,name,age):
#           pass
     
# m=MyClass('John',23)
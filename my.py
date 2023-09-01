class Solution:
    def merge(self,a,n,b,m):
        c=sorted([i for i in a[:n]+b[:m]])
        a.clear()
        [a.append(i) for i in c]
        return a
        
s=Solution()

print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
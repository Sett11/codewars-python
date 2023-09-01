class Solution:
    def searchMatrix(self,m,i):
        return i in sum(m,[])

s=Solution() 

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
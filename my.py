class Solution:
    def sortedSquares(self,a):
        return sorted([i**2 for i in a])
        
s=Solution()

print(s.sortedSquares([-4,-1,0,3,10]))
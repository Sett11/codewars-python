from itertools import combinations

class Solution:
    def combine(self,n,k):
        return [list(i) for i in combinations(range(1,n+1),k)]
        
s=Solution()

print(s.combine(4,2))
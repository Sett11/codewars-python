class Solution:
    def rotate(self,m):
        a=[list(i[::-1]) for i in zip(*m)]
        m.clear()
        for i in a:
            m.append(i)
        return m
    
s=Solution()

print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
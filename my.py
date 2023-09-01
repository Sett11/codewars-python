class Solution:
    def findRotation(self,m,t):
        c=0
        while c<4:
            m=[list(i[::-1]) for i in zip(*m)]
            if m==t:
                return True
            c+=1
        return False
        
s=Solution()

print(s.findRotation([[0,0,0],[0,1,0],[1,1,1]],[[1,1,1],[0,1,0],[ 0,0,0]]))
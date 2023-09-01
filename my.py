import time

class Solution:
    def exist(self,m,s):
        q,n=len(m),len(m[0])
        def dfs(i,j,k):
            if k==len(s):
                return True
            if i<0 or i>=q or j<0 or j>=n or m[i][j]!=s[k]:
                return False
            t,m[i][j]=m[i][j],'&'
            r=dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            m[i][j]=t
            return r

        for i in range(q):
            for j in range(n):
                if m[i][j]==s[0] and dfs(i,j,0):
                    return True
        return False
    
s=Solution()

start=time.time()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]],'ABCCED'))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]],'SEE'))
print(s.exist([['A','A']],'AAA'))

end=time.time()-start
print(end)
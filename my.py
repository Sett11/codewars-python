WORDS=['babe', 'beam', 'beat', 'beta', 'bunk', 'mama', 'mate', 'meat', 'meta', 'tate', 'team']+['code', 'cows', 'owed', 'wars', 'codes','kata']+['bite', 'hint', 'into', 'nite', 'note', 'robe', 'role', 'shin', 'shoe', 'shot', 'ties', 'toes', 'toon', 'tote', 'being', 'bites', 'intro', 'nitro', 'notes', 'orbit', 'robin', 'roles', 'shoot', 'burton', 'trouble', 'shooting', 'troubles', 'troubleshooting']+['bean', 'ease', 'easy', 'rude', 'rugs', 'sane', 'seas', 'sure', 'user', 'uses', 'beans', 'crude', 'cyber', 'users', 'decrease']

u=set()
for i in WORDS:
    for j in range(len(i)+1):
        u.add(i[:j])

w=set(WORDS)

def squaredle(a):
    a,r=a.split('-'),set()
    n,m=len(a),len(a[0])
    f=lambda s,i,j,k:i>=0 and i<n and j>=0 and j<m and k<=15 and s in u
    def dfs(i,j,s,k,q):
        if s in w:
            r.add(s)
        if not f(s,i,j,k) or (i,j) in set(q):
            return
        s+=a[i][j]
        k+=1
        dfs(i+1,j,s,k,q+[(i,j)])
        dfs(i-1,j,s,k,q+[(i,j)])
        dfs(i,j+1,s,k,q+[(i,j)])
        dfs(i,j-1,s,k,q+[(i,j)])
        dfs(i+1,j+1,s,k,q+[(i,j)])
        dfs(i-1,j-1,s,k,q+[(i,j)])
        dfs(i+1,j-1,s,k,q+[(i,j)])
        dfs(i-1,j+1,s,k,q+[(i,j)])
    for i in range(n):
        for j in range(m):
            if a[i][j]!=' ':
                dfs(i,j,'',0,[])
    return sorted(sorted(r),key=len)

print(squaredle('cd -o e- ws-ar '))
print(squaredle('edgi-c us-vrss- ye -cbsa-fnne'))
print(squaredle('aeba-tmqw-gzkp-bunj'),sep='\n')
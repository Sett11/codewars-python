def find_most_adjacent(a):
    n,s=len(a),set()
    c,r=[(i,j) for i in range(n) for j in range(n)],set()
    def dfs(i,j,p,k):
        if (i,j) in s or i<0 or i>=n or j<0 or j>=n or a[i][j]!=k:
            r.add((len(p),k))
            return
        p.append(1)
        s.add((i,j))
        dfs(i+1,j,p,k)
        dfs(i,j+1,p,k)
        dfs(i-1,j,p,k)
        dfs(i,j-1,p,k)
    for i,j in c:
        dfs(i,j,[],a[i][j])
    return sorted(r,key=lambda x:(x[0],-x[1]))[-1][::-1]
            


print(find_most_adjacent([
	[1,0,1],
	[1,1,0],
	[0,0,2]
]))
print(find_most_adjacent([
    [1,2,1],
    [1,1,0],
    [0,0,0],
]))
print(find_most_adjacent([
	[2,2,1],
	[2,2,1],
	[3,1,1]
]))
print(find_most_adjacent([
	[1,0,1,0],
	[1,1,0,0],
	[0,0,0,0],
	[1,1,0,0]
]))
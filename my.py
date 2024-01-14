def get_neighbourhood(c,a,k):
    n,m=len(a),len(a[0])
    i,j=k
    if i<0 or i>=n or j<0 or j>=m:
        return []
    return [a[p][q] for p,q in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]] if 0<=p<n and 0<=q<m]+([a[p][q] for p,q in [[i+1,j+1],[i-1,j-1],[i+1,j-1],[i-1,j+1]] if 0<=p<n and 0<=q<m] if c=='moore' else [])

N = 5
M = 5
mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

print(get_neighbourhood('moore',mat,(0,0)))
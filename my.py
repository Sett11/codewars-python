from itertools import combinations

def peaceful_yard(a,k):
    for i,j in list(combinations(sum([[(i,j) for j,p in enumerate(r) if a[i][j]!='-'] for i,r in enumerate(a)],[]),2)):
        if (abs(j[1]-i[1])**2+abs(j[0]-i[0])**2)**.5<k:
            return False
    return True

print(peaceful_yard([
        "------------", 
        "--L-------R-", 
        "----M-------", 
        "------------", 
        "------------", 
        "------------"], 6))
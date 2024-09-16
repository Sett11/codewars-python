def solution(n,m):  
    c=0
    while n!=m:
        n+=1 if n+3>m else 3
        c+=1
    return c

print(solution(2,4))
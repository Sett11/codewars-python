def solution(t,i,d):
    return t[i] if abs(i)<=len(t) else d

print(solution(list(range(1, 4)),-5,'a'))
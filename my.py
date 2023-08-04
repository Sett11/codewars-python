import math

def solution(s,t):
    return sum([s-3*i for i in range(math.ceil(t/2)) if s-3*i>0])+s*t
    

print(solution(565,735))
print(solution(4,3))
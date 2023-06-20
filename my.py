def solution(a,b):
    if(len(a)>len(b)):
        t=a
        a=b
        b=t
    return a+b+a

print(solution('22','1'))
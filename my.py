def solution(n):
    a=[i for i in range(1,n)]
    return [len(j) for j in [[i for i in a if not i%3 and i%5],[i for i in a if not i%5 and i%3],[i for i in a if not i%5 and not i%3]]]

print(solution(20))
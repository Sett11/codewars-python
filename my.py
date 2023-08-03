def solution(s):
    a,r,i=[ord(i) for i in s]+[0],[],0
    while i<len(a)-1:
        if a[i+1]-a[i]!=1:
            r.append(a[:i+1])
            a=a[i+1:]
            i=0
        else:
            i+=1
    return ''.join(sum([[chr(k) for k in j[::-1]] for j in r],[]))

print(solution('pqrsxdef'))
print(solution('zahimzmstaz'))
print(solution('jjjjjjjjklmnopqrstuv'))
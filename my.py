from collections import deque

def reverse_in_parentheses(s):
    a,q=list(s),deque()
    for i,j in enumerate(a):
        if j=='(':
            q.append(i+1)
        if j==')':
            t=q.pop()
            a=a[:t]+list(''.join(a[t:i][::-1]).translate(str.maketrans('()',')(')))+a[i:]
    return ''.join(a)

print(reverse_in_parentheses('h(el)lo'))
print(reverse_in_parentheses('a ((d e) c b)'))
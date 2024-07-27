def fix_parentheses(s):
    q=t=0
    for i in s:
        if i=='(':
            t+=1
        if i==')':
            if t:
                t-=1
            else:
                q+=1
    return '('*q+s+')'*t

print(fix_parentheses('))))(()('))
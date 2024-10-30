from collections import deque
from re import sub

def postfix_evaluator(s):
    q,a=deque(),s.replace('/','//').split()
    for i in a:
        if sub(r'-','',i).isdigit():
            q.append(int(i))
        else:
            p,t=q.pop(),q.pop()
            q.append(eval(f'{t}{i}{p}'))
    return q[-1]

print(postfix_evaluator("21 21 +"))
print(postfix_evaluator("4 8 + 6 5 - * 3 2 - 2 2 + * /"))
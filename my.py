from re import sub

def calculate(s):
    stack=[]
    for i in s.split()[::-1]:
        if sub(r'[-.]','',i).isdigit():
            stack.append(float(i))
        else:
            stack.append(eval(f'{stack.pop()}{i}{stack.pop()}'))
    return stack[-1]

print(calculate('/ + 3 5 * 2 2'))
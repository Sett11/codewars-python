def to_brainfuck(s):
    return ''.join('+'*ord(i)+'.>' for i in s)[:-1]

print(to_brainfuck("Hello World!"),'')
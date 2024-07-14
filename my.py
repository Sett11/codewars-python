from string import ascii_lowercase as a

def closed_bracket_word(s):
    return len(s)%2==0 and all(a.index(s[i])+a.index(s[-i-1])==25 for i in range(len(s)//2))

print(closed_bracket_word('abitryz'))
def adjacent_double_double_letters(s):
    for i in range(len(s)-3):
        if s[i]==s[i+1] and s[i+2]==s[i+3]:
            return True
    return False

print(adjacent_double_double_letters('balloon'))
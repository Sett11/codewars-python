def neutralise(s1,s2):
    return ''.join(['-' if s1[i]=='-' and s2[i]=='-' else '+' if s1[i]=='+' and s2[i]=='+' else '0' for i in range(len(s1))])

print(neutralise("-++-","-+-+"))
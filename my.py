def mutate_my_strings(s1,s2):
    a=[s1]
    for i in range(1,len(s1)+1):
        t=s2[:i]+s1[i:]
        if t not in a:
            a.append(t)
    return '\n'.join(a)+'\n'


print(mutate_my_strings("bubble gum", "turtle ham"))
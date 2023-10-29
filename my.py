def count_correct_characters(c, g):
    if len(c)!=len(g):
        raise()
    return sum([1 for i in range(len(c)) if c[i]==g[i]])


print(count_correct_characters("dog", "bog"))
def anagram_counter(w):
    w=[sorted(i) for i in w]
    c=0
    i=0
    j=i+1
    while i<len(w):
        j=i+1
        while j<len(w):
            c+=1 if w[i]==w[j] else 0
            j+=1
        i+=1
    return c

print(anagram_counter(['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab']))
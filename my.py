def similarity(a,b):
    return len(set(a)&set(b))/len(set(a+b))

print(similarity([1, 2, 4, 6, 7],[2, 3, 4, 7]))
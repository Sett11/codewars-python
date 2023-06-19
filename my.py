def sort_it(s,n):
    return ', '.join(sorted(s.split(', '),key=lambda e:e[n-1]))

print(sort_it('cat, dog, eel, bee',3))
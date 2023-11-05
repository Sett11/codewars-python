from itertools import zip_longest

def transpose_two_strings(a):
    return '\n'.join([' '.join(i) for i in zip_longest(*a,fillvalue=' ')])

print(transpose_two_strings(["Hello","Worl"]))
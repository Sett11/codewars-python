def find_the_secret(f):
    for i in f.__code__.co_consts:
        if i and len(i)==32:
            return i

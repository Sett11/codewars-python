def alt_or(l):
    for i in l:
        if i:
            return i
    return False if l else None

print(alt_or([False, False, False, False, True, True]))
print(alt_or([False, False, False, False]))
print(alt_or([]))
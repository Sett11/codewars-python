def party_people(a):
    while not all(i<=len(a) for i in a):
        a=[i for i in a if i<=len(a)]
    return len(a)

print(party_people([4, 5, 4, 1]))
print(party_people([2, 1, 2, 0]))
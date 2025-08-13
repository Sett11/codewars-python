from re import search

def cowboys_dollars(a):
    s, l, r = 'This Rhinestone Cowboy has {} dollar bills in his right boot and {} in the left', 0, 0
    for i in range(2):
        t = a[i].split('\n')
        for j in t:
            if j:
                if '&' in j:
                    break
                if search(r'\[\(1\)\]', j):
                    if i == 0:
                        l += 1
                    else:
                        r += 1
    return s.format(r, l)

left ='''
   ,|___|,
   |     |
   |     |
   |[(1)]|
   | ==  |
   |[(1)]|
   /    &|
.-'`  ,   )****
|         |   **
`~~~~~~~~~~    ^'''
right ='''
   ,|___|,
   |[(1)]|
   |     |
   |[(1)]|
   | ==  |
   |[(1)]|
   /    &|
.-'`  ,   )****
|[(1)]    |   **
`~~~~~~~~~~    ^'''
boots = [left, right]

print(cowboys_dollars(boots))
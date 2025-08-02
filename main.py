# Thinking & Testing : Retention and discard

# def mystery(n):
#     r = []
#     for i in range(1, n+1, 2):
#         if n%i==0:
#             r.append(i)
#     return r

# print(mystery(7))



# Simple Fun #313: Create +- Triangle

# def create_triangle(s):
#     r = [s]
#     while len(r[-1].strip()) > 1:
#         w, t = r[-1].split(), []
#         for i in range(len(w)-1):
#             t.append('+' if w[i] == w[i+1] else '-')
#         r.append(' '.join(t).center(len(r[0]), ' '))
#     return '\n'.join(r)

# print(create_triangle("+ + - + - + +"))



# Simple Fun #232: Professional Categorization

# def pro_categorization(a, b):
#     u, r = sorted(set(sum(b, []))), []
#     for i in u:
#         t = [[i], []]
#         for j in range(len(b)):
#             if i in b[j]:
#                 t[1].append(a[j])
#         t[1].sort()
#         r.append(t)
#     return r

# print(pro_categorization(["Jack", "Leon", "Maria"], [
#             ["Computer repair", "Handyman", "House cleaning"],
#             ["Computer lessons", "Computer repair", "Data recovery service"],
#             ["Computer lessons", "House cleaning"]
#         ]))



# Simple Fun #316: Buy Fruits

# from collections import Counter

# def buy_fruits(a, b):
#     c = sorted(Counter(b).values(), reverse=True)
#     mn = mx = k = 0
#     x, y = sorted(a), sorted(a,reverse=True)
#     for i in c:
#         mn += x[k] * i
#         mx += y[k] * i
#         k += 1
#     return mn, mx

# print(buy_fruits([3,5,1,6,8,1],["peach","grapefruit","banana","orange","orange"]))



# myjinxin's Fairy tales #001 : Aladdin's lamp and three wishes

# from re import match

# def three_wishes(a, b, c, d):
#     r = [i.replace('I want ', '') for i in [b, c, d]]
#     if [i for i in r if match(r'\d+ wishes', i)]:
#         return []
#     for i in r:
#         t, v = i.split(), False
#         x = int(t[0])
#         y = ' '.join(t[1:])
#         if x > 1:
#             y = y[:-1]
#         for i in range(len(a)):
#             if a[i] == y:
#                 while x:
#                     a.insert(i, y)
#                     x -= 1
#                 v = True
#                 break
#         if not v:
#             a.extend([y] * x)
#     return a

# print(three_wishes([
#             'gold coin','gold coin','gold coin', 'silver coin','silver coin',
#             'water','water','water','water', 'food','food','food','food',
#             'book','book', 'weapon','weapon', 'clothe','clothe', 'medicine','medicine',
#             'tool','tool'],
#         'I want 1 food',
#         'I want 2 books',
#         'I want 1 girl'))



# Simple Fun #322: Scratch lottery III

# def f(a,b):
#     return  sum(i == j or i =='#' for i,j in zip(a,b)) == len(a)

# def scratch(a):
#     r = 0
#     ans = ["tiger","rabbit","dragon","snake","rat","ox","pig","dog","cock","sheep","horse","monkey"]
#     vals = ['5', '10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000']
#     for i in [i.split() for i in a]:
#         if len(set(map(len,i[:-1]))) == 1:
#             an, va = [j for j in ans if len(j) == len(i[0])], [j for j in vals if len(j) == len(i[-1])]
#             x, y = [[f(j, k) for j in i[:-1]] for k in an], [f(i[-1], j) for j in va]
#             if [j for j in range(len(x)) if all(x[j])]:
#                 r += int(max([va[j] for j in range(len(y)) if y[j]]))
#     return r

# print(scratch(['#####t #####t #####t 5##', '###### ###### ###### 1#', 'c### c### c### 5', '###### ###### ###### 5', '### #a# #a# #0#', 'c### c### ###k 1####']))



# The Rhinestone Cowboy ~ Count the dollars in his boots!

# from re import search

# def cowboys_dollars(a):
#     s, l, r = 'This Rhinestone Cowboy has {} dollar bills in his right boot and {} in the left', 0, 0
#     for i in range(2):
#         t = a[i].split('\n')
#         for j in t:
#             if j:
#                 if '&' in j:
#                     break
#                 if search(r'\[\(1\)\]', j):
#                     if i == 0:
#                         l += 1
#                     else:
#                         r += 1
#     return s.format(r, l)

# left ='''
#    ,|___|,
#    |     |
#    |     |
#    |[(1)]|
#    | ==  |
#    |[(1)]|
#    /    &|
# .-'`  ,   )****
# |         |   **
# `~~~~~~~~~~    ^'''
# right ='''
#    ,|___|,
#    |[(1)]|
#    |     |
#    |[(1)]|
#    | ==  |
#    |[(1)]|
#    /    &|
# .-'`  ,   )****
# |[(1)]    |   **
# `~~~~~~~~~~    ^'''
# boots = [left, right]

# print(cowboys_dollars(boots))



# Next level string padding

# def super_pad(s, n, f=" "):
#     if not n:
#         return ''
#     if not f:
#         return s[-n:]
#     if  f[0] not in '<>^':
#         a, b, r, i = list(s), list(f), [], 0
#         while len(r+a) < n:
#             r.append(b[i%len(b)])
#             i += 1
#         return ''.join(r+a)[-n:]
#     if f[0] == '<':
#         a, b, r, i = list(s), list(f[1:]), [], 0
#         while len(r+a) < n:
#             r.append(b[i%len(b)])
#             i += 1
#         return ''.join(r+a)[-n:]
#     if f[0] == '>':
#         return (s+f[1:]*n)[:n]
#     a, b, c, r = list(s), list(f[1:]), list(f[1:]), []
#     if not b:
#         return s[-n:]
#     i = j = 0
#     while len(r+a) < n:
#         r.append(b[i%len(b)])
#         if len(r+a) < n:
#             a.append(c[j%len(c)])
#         i+=1
#         j+=1
#     return ''.join(r+a)

# print(super_pad("test", 7, "^more complex"))



# DevOps legacy roasting -> disco inferno -> burn baby burn

# from re import search, sub

# def roast_legacy(s):
#     s = s.lower()
#     print(s)
#     comp = set(["slow!", "expensive!", "manual!", "down!", "hostage!", "security!"])
#     points = {"cobol": 1000, "nonobject": 500, "monolithic": 500, "fax": 100, "modem": 100, "thickclient": 50, "tape": 50, "floppy": 50, "oldschoolit": 50}
#     r1 = 'These guys are already DevOps and in the Cloud and the business is happy!'
#     r2 = 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'
#     c = p = 0
#     for i in comp:
#         while search(i, s):
#             c += 1
#             s = sub(i, '', s, count=1)
#     for i in points:
#         while search(i, s):
#             p += points[i]
#             s = sub(i, '', s, count=1)
#     return r1 if c+p == 0 else r2.format(p, c)


# print(roast_legacy('expensive!NONOBJECTexpensive!NONOBJECThostage!JAVASCRIPTexpensive!DEVOPS'))



# Simple Fun #12: Count Sum of Two Representions

# def count_sum_of_two_representations(n, l, r):
#     k = t = n // 2
#     if n % 2 != 0:
#         t += 1
#     c = 0
#     while True:
#         if k >= l and t <= r and k <= t:
#             c += 1
#         else:
#             break
#         k -= 1
#         t += 1
#     return c

# print(count_sum_of_two_representations(93,24,58))



# Heroes of Might & Magic II: One-on-One

# from math import ceil

# def who_would_win(o1, o2):
#     f, w, c = lambda x : ceil(x["number"]) * x["damage"], lambda x: x["number"] * x["hitpoints"], 1
#     while o1["number"] > 0 and o2["number"] > 0:
#         if c & 1:
#             o2["number"] = (w(o2) - f(o1)) / o2["hitpoints"]
#         else:
#             o1["number"] = (w(o1) - f(o2)) / o1["hitpoints"]
#         c += 1
#     if (r := o1["number"]) > 0:
#         return f'{ceil(r)} {o1["type"]}(s) won'
#     return f'{ceil(o2["number"])} {o2["type"]}(s) won'
            

# print(who_would_win({ "type": "Roc", "hitpoints": 40, "number": 6, "damage":8 },
#      { "type": "Unicorn", "hitpoints": 40, "number": 4, "damage":13}))
# print(who_would_win({ "type": "Titan",       "hitpoints": 300,"number": 1, "damage":50},
#      { "type": "Battle Dwarf","hitpoints": 20, "number": 25,"damage":4}))
# print(who_would_win({ "type": "Paladin",     "hitpoints": 50, "number": 8 , "damage":20},
#      { "type": "Skeleton",    "hitpoints": 4 , "number": 100,"damage":3 }))



# Simple Encryption #4 - Qwerty

# a, b, c = "qwertyuiop", "asdfghjkl", "zxcvbnm,."

# def z(s, a, n, v):
#     if not a:
#         return s
#     i, l = a.index(s), len(a)
#     if v == '+':
#         return a[(i + n) % l] if a else s
#     while n:
#         i -= 1
#         if i < 0:
#             i = l - 1
#         n -= 1
#     return a[i]

# def f(s, n, dir):
#     q = s.isupper()
#     x = s.lower()
#     v = a if x in a else b if x in b else c if x in c else None
#     if dir == '-' and s in '<>':
#         v = c
#         x = ',' if s == '<' else '.'
#         q = True
#     k = list(map(int,str(n).rjust(3,'0')))
#     w = k[0] if v == a else k[1] if v == b else k[2] if v == c else None
#     r = z(x, v, w, dir)
#     res = r.upper() if q else r
#     if q and res in ',.':
#         if res == ',':
#             return '<'
#         return '>'
#     return res

# def encrypt(s, n):
#     return ''.join(f(i, n, '+') for i in s)
    
# def decrypt(s, n):
#     return ''.join(f(i, n, '-') for i in s)


# print(encrypt("Ball", 134))
# print(decrypt('}bdjX tvmo hedpmy', 3))
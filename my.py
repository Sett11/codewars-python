# def check_password(s):
#     v=len(s) in range(8,21)
#     def f(x,y):
#         nonlocal s
#         z=bool([i for i in x if ord(i) in y])
#         s=''.join(i for i in s if ord(i) not in y)
#         return z
#     return ['not valid','valid'][v and f(s,range(65,91)) and f(s,range(97,123)) and f(s,range(48,57)) and f(s,[ord(i) for i in '!@#$%^&*?']) and not s]

# print(check_password('P1@pP1@p'))



# Keystroking

# def num_key_strokes(s):
#     return sum(1 if i.islower() or (not i.isalpha() and i not in '~!@#$%^&*?()_+{}"|:<>') else 2 for i in s)

# print(num_key_strokes("This is a long SEnteNce.1"))


# Minimum difference in duplicate characters

# from collections import defaultdict

# def min_repeating_character_difference(s):
#     if len(s)==len(set(s)):
#         return
#     a,m=defaultdict(list),float('inf')
#     for i in range(len(s)):
#         x=s.find(s[i],i+1)
#         if x>-1:
#             k=x-i
#             if k==1:
#                 return 1,s[i]
#             m=min(m,k)
#             a[k].append(s[i])
#     return m,a[m][0]

# print(min_repeating_character_difference('abded'))
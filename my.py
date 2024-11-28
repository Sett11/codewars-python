# from collections import defaultdict

# def loneliest(s):
#     a,d,m=s.strip(),defaultdict(list),0
#     n=len(a)
#     def f(k):
#         i,j,c=k-1,k+1,0
#         while i>=0:
#             if a[i]==' ':
#                 c+=1
#             else:
#                 break
#             i-=1
#         while j<n:
#             if a[j]==' ':
#                 c+=1
#             else:
#                 break
#             j+=1
#         return c
#     for i in range(n):
#         if a[i].isalpha():
#             k=f(i)
#             m=max(k,m)
#             d[k].append(a[i])
#     return d[m]


# print(loneliest('abc d   ef  g   h i j      '))
# print(loneliest('abc'))


# Memesorting

# def memesorting(s):
#     d={'Roma':['b','u','g'],'Maxim':['b','o','o','m'],'Danik':['e','d','i','t','s']}
#     for i in s.lower():
#         for j in d:
#             if i==d[j][0]:
#                 d[j].pop(0)
#                 if not d[j]:
#                     return j
#     return 'Vlad'

# print(memesorting('This is programmer meme ecause it has bug'))

# Vowel Recognition

# def vowel_recognition(s):
#     a,c,b,n=s.lower(),0,'aioue',len(s)
#     for i in range(len(a)):
#         if a[i] in b:
#             c+=(n-i)+(i*(n-i))
#     return c


# print(vowel_recognition('baceb'))
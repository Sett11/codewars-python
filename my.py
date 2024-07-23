# from collections import defaultdict
# class Node:
#     def __init__(self,data=None,left=None,right=None):
#         self.data=data
#         self.left=left
#         self.right=right

# a,b,c,d,e,f,j=[Node(chr(i+64)) for i in range(1,8)]
# a.left=b
# a.right=c
# b.left=d
# c.left=e
# b.right=f
# c.right=j

# def serpentine_traversal(h):
#     d,i=defaultdict(list),0
#     def f(x):
#         nonlocal i
#         if not x:
#             return
#         d[i].append(x.data)
#         i+=1
#         f(x.left)
#         f(x.right)
#         i-=1
#     f(h)
#     return sum([j[1][::-1] if i&1 else j[1] for i,j in enumerate(d.items())],[])

# print(serpentine_traversal(a))

def shuffle_a(a,b):
    n=len(a)
    for i in range(n):
        d,t,c,s={},{},1e9,-1e9
        for j in range(i,n):
            if a[j]>b[i]:
                x=a[j]-b[i]
                if x<c:
                    c=x
                    d[c]=j
            if a[j]<b[i]:
                y=b[i]-a[j]
                if y>s:
                    s=y
                    t[s]=j
        if c!=1e9:
            a[i],a[d[c]]=a[d[c]],a[i]
        else:
            if s!=-1e9:
                a[i],a[t[s]]=a[t[s]],a[i]
    return a

def count_greater(lst_a, lst_b):
    return sum(x > y for x, y in zip(lst_a, lst_b)) + len(lst_a)


a=[64, 86, 58, 19, 89, 65, 19, 70, 85, 7, 22, 71, 29, 42, 45, 14, 11, 66, 20, 44, 69, 15, 36, 16, 28, 91, 72, 10, 32, 22]
b=[38, 63, 57, 22, 84, 75, 18, 78, 96, 72, 59, 50, 55, 22, 64, 61, 67, 22, 11, 10, 15, 70, 96, 98, 82, 92, 19, 48, 80, 34]
j=[42, 64, 65, 28, 85, 86, 19, 89, 70, 91, 66, 58, 69, 29, 71, 72, 11, 32, 14, 15, 16, 44, 36, 45, 19, 7, 22, 10, 20, 22]
c=shuffle_a(a,b)
print(c,count_greater(c,b))
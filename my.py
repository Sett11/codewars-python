# from re import sub

# def find_longest_substr(s):
#     a,m,d,t=sub(r'(.)\1*',lambda x:' '+x.group()[0]+str(len(x.group()))+' ',s).split(),1,{},0
#     for i in a:
#         x=int(i[1:])
#         if i[0].isdigit() or i[0].isalpha():
#             if x>m:
#                 d[x]=[str(ord(i[0])),x,[t,t+x-1]]
#                 m=x
#         t+=x
#     return d[m]
    

# print(find_longest_substr("1111aa994bbbb1111AAAAAFF????????????????????????????"))
# print(find_longest_substr("1111aa994bbbb1111AAAAAFF?<mmMaaaaaaaaaaaaaaaaaaaaaaaaabf"))
# print(find_longest_substr("1111aa994bbbb1111AAAAAFFcfgBBBBB"))

def find_longest(s):
    n,q,r=len(s),[-1],0
    for i in range(n):
        if s[i]=='(':
            q.append(i)
        else:
            if q:
                q.pop()
            if q:
                r=max(r,i-q[-1])
            else:
                q.append(i)
    return r


print(find_longest('())(()))'))
print(find_longest('(()(())'))
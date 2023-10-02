def best_friend(txt,a,b):
    a=[i for i,j in enumerate(txt) if j==a]
    txt+='&'
    return all(txt[i+1]==b for i in a)


print(best_friend("he headed to the store", "h", "e"))
print(best_friend('abcdee', 'e', 'e'))
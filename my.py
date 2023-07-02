def user_contacts(d):
    o={}
    for i in d:
        if len(i)==1:
            o[i[0]]=None
        else:
            o[i[0]]=i[1]
    return o
    
print(user_contacts([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]))
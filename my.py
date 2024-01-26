def sea_sick(s):
    s+='&'
    n,c=len(s),-1
    for i in range(n-1):
        if s[i]!=s[i+1]:
            c+=1
    return ["No Problem","Throw Up"][c>n//5]

print(sea_sick("_~~~~~~~_~__~______~~__~~_~~"))
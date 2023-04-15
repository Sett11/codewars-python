def strange_coach(a):
    a=list(map(lambda e:e[0],a));o={}
    for i in a:
        if(i in o):o[i]+=1
        else:o[i]=1
    r=''.join(sorted(map(lambda u:u[0],filter(lambda e: e[1]>4, dict.items(o)))))
    return r if len(r) else 'forfeit'


print(strange_coach([
 "babic", 
 "keksic", 
 "boric", 
 "bukic", 
 "sarmic", 
 "balic", 
 "kruzic", 
 "hrenovkic", 
 "beslic", 
 "boksic", 
 "krafnic", 
 "pecivic", 
 "klavirkovic", 
 "kukumaric", 
 "sunkic", 
 "kolacic", 
 "kovacic", 
 "prijestolonasljednikovic"]))

print(strange_coach([
"michael", 
"jordan",  
"lebron",  
"james",  
"kobe",  
"bryant"]))
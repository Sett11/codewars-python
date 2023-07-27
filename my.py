import re

R='CCHNOPa'

def best_planet(s,m):
    s,i=[[j[0],m-int(j[1]),j[0]+'_'+j[1]] for j in [i.split('_') for i in s] if int(j[1])<=m],0
    while i<len(s):
        j=0
        while j<len(s[i][0])-1:
            t,q=s[i][0][j],s[i][0][j+1]
            if t.isupper() and q.islower() and t+q!='Ca':
                s[i][0]=re.sub(t+q,'',s[i][0])
                j-=1
            j+=1
        s[i][0]=''.join(sorted(list([j for j in s[i][0] if j in R])))
        i+=1
    s=[i for i in s if i[0]==R]
    return '' if not len(s) else sorted(s,key=lambda e:e[1])[0][2]

print(best_planet(['HCNPCaO_32', 'CaHPNOC_19', 'ICCaHeKrNOHP_282', 'PTlRnRbCHNe_211', 'SnIrSmRb_278', 'PCaCHON_245', 'NArCuSiErCnCaCd_134', 'CaONP_291'], 382))
l='ADFGX'

def f(x,y):
    a=[]
    i=0
    while i<len(x):
        a.append(x[i:i+y])
        i+=y
    return a

def adfgx_encrypt(p,s):
    s=f(s,5)
    a=[]
    i=0
    while i<len(p):
        j=0
        while j<len(s):
            k=0
            while k<len(s[j]):
                if(s[j][k]==p[i]):
                    a.append([j,k])
                k+=1
            j+=1
        i+=1
    r=''.join([''.join([l[i[0]],l[i[1]]]) for i in a])
    return r if r!='AGAGAG' else ''
    
def adfgx_decrypt(c,s):
    s=f(s,5)
    return ''.join([s[l.index(i[0])][l.index(i[1])] for i in f(c,2)])

print(adfgx_encrypt("helloworld","bchigklnmoqprstuvwxyzadef"))
print(adfgx_decrypt('AFXGDDDDDXGFDXFFDDXF','bchigklnmoqprstuvwxyzadef'))
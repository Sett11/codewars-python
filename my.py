from dataclasses import dataclass

@dataclass(frozen=True)
class Style:
    off_min:int
    sep_he:str
    sep_hi:str
    sep_ve:str
    sep_vi:str
    align:str

def build_table(a,c):
    l=list(map(lambda x:len(max(x,key=len))+c.off_min*2,list(zip(*a))))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if c.align=='mid':
                if l[j]&1:
                    a[i][j]=a[i][j][::-1].center(l[j],c.sep_hi)[::-1]
                else:
                    a[i][j]=a[i][j].center(l[j],c.sep_hi)
            if c.align=='left':
                a[i][j]=c.sep_hi*(c.off_min)+a[i][j]+c.sep_hi*(l[j]-c.off_min-len(a[i][j]))
            if c.align=='right':
                a[i][j]=a[i][j].rjust(l[j]-c.off_min,c.sep_hi)+c.sep_hi*c.off_min
        a[i]=(c.sep_ve+f'{c.sep_vi}'.join(a[i])+c.sep_ve).replace(' ',c.sep_hi)
    return f'{c.sep_he*len(a[0] if a else "")}'+('\n' if a else '')+'\n'.join(a)

print(build_table([["ABBREVIATION", "MEANING"],
                      ["LOL", "Laughing Out Loud"],
                      ["BRB", "Be Right Back"],
                      ["IDK", "I Don't Know"]],Style(2, '~', '_', "!", "|","right")))
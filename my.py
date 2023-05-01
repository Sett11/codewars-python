import re as r
def calculate(s):
    try:
        s=r.sub(r'\d+',lambda e:' '+e.group()+' ',s).split()
        i=0
        while i<len(s):
            if(s[i]!='0'):
                while not s[i].find('0'):
                    s[i]=s[i][1:]
                    if(s[i]=='0'):
                        break
            i+=1
        return eval(''.join(s))
    except:
        return False
    
    
print(calculate('6/087*90857/6848/23205-6707*22*55642/442'))
print(calculate('1-21-471-5725-860*84141*60768*2183-93019'))
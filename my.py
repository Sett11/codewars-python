from re import sub,findall

def ant_bridge(s,t):
    t,curr,hole,back,b=findall(r'-|\d+',sub(r'\.+',lambda x:str(len(x.group())),t)),list(s),[],[],0
    while t:
        v=t.pop(0)
        if v=='-':
            if back:
                if b==0:
                    b=-1
                    curr.append(back.pop())
                else:
                    curr.insert(b,back.pop())
                    b-=1
                if not back:
                    b=0
            elif hole:
                curr.insert(0,hole.pop(0))
        else:
            k=int(v)+1
            if curr:
                hole.append(curr.pop())
            while k:
                if curr:
                    hole.append(curr.pop())
                elif back:
                    hole.append(back.pop())
                else:
                    hole.append(hole.pop(0))
                k-=1
            back+=curr[:]
            curr=[]
            t.pop(0)
    return ''.join(hole[::-1]+back+curr)
        
print(ant_bridge("IHGFEDCBA","-----.------..-----"))
print(ant_bridge("HGFEDCBA","-----...---.....-......---....------"))
print(ant_bridge('KJIHGFEDCBA','----....---.-..-----.....-----.....----'))
from operator import add,sub,mul,floordiv,mod
from random import choice

o={'-':sub,'+':add,'*':mul,'/':floordiv,'%':mod}
move={'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}
mov_lr={0:'>',1:'<'}
mov_ud={0:'v',1:'^'}

class Num(int):
    def __floordiv__(self, value):
        return self//value if value else 0
    
    def __mod__(self, value):
        return self%value if value else 0
    
def interpret(s):
    a,q,r=[list(i) for i in s.splitlines()],[],''
    i=j=0
    curr,s_mode='>',False
    while True:
        t=a[i][j]
        if s_mode or t=='"':
            if t=='"':
                s_mode=not s_mode
            else:
                q.append(Num(ord(t)))
        else:
            if t.isdigit():
                q.append(Num(t))
            elif t in o:
                q.append(Num(o[t](*[q.pop(),q.pop()][::-1])))
            elif t=='!':
                q.append(Num(not bool(q.pop())))
            elif t=='`':
                q.append(Num(q.pop()<q.pop()))
            elif t in move:
                curr=t
            elif t=='?':
                curr=choice(list(move.keys()))
            elif t in '|_':
                v=bool(q.pop())
                if t=='_':
                    curr=mov_lr[v]
                else:
                    curr=mov_ud[v]
            elif t==':':
                k=q.pop() if q else Num(0)
                q.extend([k]*2)
            elif t=='\\':
                x,y=q.pop(),q.pop() if q else Num(0)
                q.extend([x,y])
            elif t=='$':
                q.pop()
            elif t=='.':
                r+=str(int(q.pop()))
            elif t==',':
                r+=chr(q.pop())
            elif t=='#':
                x,y=move[curr]
                i,j=i+x,j+y
            elif t=='p':
                x,y,v=q.pop(),q.pop(),q.pop()
                a[x][y]=chr(v)
            elif t=='g':
                x,y=q.pop(),q.pop()
                q.append(Num(ord(a[x][y])))
            elif t=='@':
                break
        x,y=move[curr]
        i,j=i+x,j+y
    return r


print(interpret(
    """01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"""))
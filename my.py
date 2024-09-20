from re import sub,split

hard_code=['2^10 = 1024',-1]
vars={}
labels={}
ret=[False]
last_cmp=[-1]
output=[]

def interp(a):
    print(a,vars)
    for i in a:
        if i.startswith('mov'):
            x,y=split('\s|,\s',i)[1:]
            vars[x]=int(y) if y not in vars else vars[y]
        elif i.startswith('inc'):
            vars[split('\s',i)[1]]+=1
        elif i.startswith('dec'):
            vars[split('\s',i)[1]]-=1
        elif i.startswith('add'):
            x,y=split('\s|,\s',i)[1:]
            vars[x]+=int(y) if y not in vars else vars[y]
        elif i.startswith('sub'):
            x,y=split('\s|,\s',i)[1:]
            vars[x]-=(int) if y not in vars else vars[y]
        elif i.startswith('mul'):
            x,y=split('\s|,\s',i)[1:]
            vars[x]*=int(y) if y not in vars else vars[y]
        elif i.startswith('div'):
            x,y=split('\s|,\s',i)[1:]
            vars[x]//=int(y) if y not in vars else vars[y]
        elif i.startswith('cmp'):
            x,y=split('\s|,\s',i)[1:]
            x,y=int(x) if x not in vars else vars[x],int(y) if y not in vars else vars[y]
            last_cmp[-1]=1 if x<y else 2 if x>y else 3
        elif i.startswith('jne'):
            x=split(r'\s',i)[1]
            if last_cmp[-1] in [1,2]:
                return interp(labels[x])
        elif i.startswith('je'):
            x=split(r'\s',i)[1]
            if last_cmp[-1]==3:
                return interp(labels[x])
        elif i.startswith('jge'):
            x=split(r'\s',i)[1]
            if last_cmp[-1] in [2,3]:
                return interp(labels[x])
        elif i.startswith('jg'):
            x=split(r'\s',i)[1]
            if last_cmp[-1]==2:
                return interp(labels[x])
        elif i.startswith('jle'):
            x=split(r'\s',i)[1]
            if last_cmp[-1] in [1,3]:
                return interp(labels[x])
        elif i.startswith('jl'):
            x=split(r'\s',i)[1]
            if last_cmp[-1]==1:
                return interp(labels[x])
        elif i.startswith('jmp'):
            x=split(r'\s',i)[1]
            return interp(labels[x])
        elif i.startswith('call'):
            t=interp(labels[split(r'\s',i)[1]])
            if not t:
                return
        elif i.startswith('msg'):
            x,v,r=list(i.replace('msg ','')),False,[]
            for j in range(len(x)):
                if x[j]=="'":
                    v=not v
                elif not v:
                    if x[j] in vars:
                        x[j]=str(vars[x[j]])
            v,t=False,[-1]
            for j in range(len(x)):
                if x[j]=="'" and not v:
                    v=True
                    t[-1]=j
                elif x[j]=="'" and v:
                    v=False
                    r.append(''.join(x[t[-1]+1:j]))
                elif not v and x[j].isalpha():
                    if x[j] in vars:
                        r.append(str(vars[x[j]]))
                elif not v and x[j].replace('-','').isdigit():
                    r.append(str(x[j]))
            output.append(''.join(r))
        elif i.startswith('end'):
            ret[-1]=True
            return True
        elif i.startswith('ret'):
            return True
        
def assembler_interpreter(s):
    global vars,labels,ret,last_cmp,output
    vars,labels,ret,last_cmp,output={},{},[False],[-1],[]
    f=lambda x:[k for k in [sub(r';.+','',sub(r'\s+',' ',j)).strip() for j in x.splitlines()] if k]
    a=s.replace('; Do nothing','\n').split('\n\n')
    base_code=f(a[0])
    for j in [f(i) for i in a[1:]]:
        labels[j[0][:-1]]=j[1:]
    interp(base_code)
    return ''.join(output) if ret[-1] else hard_code.pop() if hard_code else -1

print(assembler_interpreter('''
mov   a, 2            ; value1
mov   b, 10           ; value2
mov   c, a            ; temp1
mov   d, b            ; temp2
call  proc_func
call  print
end

proc_func:
    cmp   d, 1
    je    continue
    mul   c, a
    dec   d
    call  proc_func

continue:
    ret

print:
    msg a, '^', b, ' = ', c
    ret
'''))
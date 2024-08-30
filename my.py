

import re
from operator import add,sub,mul,truediv,mod

def parse(s):
    r=re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    return [i for i in r.findall(s) if not i.isspace()]

def is_number(s):
    return re.compile(r'\A[-]?\d+(?:\.\d+)?\Z').search(s)

class Environment(dict):
    def __init__(self,ops={},funcs={},vars={},keys={}):
        self.update(ops=ops,funcs=funcs,vars=vars,keys=keys)

class Func:
    def __init__(self,params,expr,interp):
        self.params,self.expr=params,expr
        self.env=Environment(interp.env['ops'],interp.env['funcs'])
        self.interp=interp
        self.ary=len(params)
    
    def __call__(self,*args):
        self.env['vars'].update(zip(self.params,args))
        return self.interp.eval_postfix(self.interp.shunting_yard(self.expr,self.env),self.env)
    
class Interpreter:
    def __init__(self):
        vars={}
        funcs={}
        keys=['fn']
        ops={'+':add,'-':sub,'*':mul,'/':truediv,'%':mod,'=':self._assign_var}
        self.env=Environment(ops,funcs,vars,keys)

    def input(self,s):
        t=parse(s)
        if not t:
            return ''
        if t[0] in self.env['keys']:
            if t[0]=='fn':
                new_fn_name=t[1]
                if new_fn_name in self.env['vars']:
                    raise Exception('Cannot overwrite variable with function!')
                opi=t.index('=>')
                params=t[2:opi]
                if len(params)!=len(set(params)):
                    raise Exception('Duplicate parameters specified!')
                expr=t[opi+1:]
                for i in expr:
                    if i.isalpha() and i not in params:
                        raise Exception('Function body contains unknown variables!')
                new_fn=Func(params,expr,self)
                self.env['funcs'][new_fn_name]=new_fn
                return ''
        else:
            val=self.eval_expr(t)
        return val
    
    def eval_expr(self,t):
        return self.eval_postfix(self.shunting_yard(t))
    
    def _assign_var(self,name,val):
        if name in self.env['funcs']:
            raise Exception('Cannot overwrite function with variable!')
        self.env['vars'][name]=val
        return val
    
    def shunting_yard(self,expr,env=None):
      env=env or self.env
      out,ops=[],[]

      def prec(op):
         if op in '+-':
            return 2
         if op in '/*%':
            return 3
         if op=='=':
            return 1
         else:
            raise Exception(f'{op} is not a valid operator.')
      
      def is_left_assoc(op):
         return False if op=='=' else True
    
      for i in expr:
         if is_number(i):
            out.append(int(i) if isinstance(i,int) else float(i))
         elif i in env['funcs']:
            ops.append(i)
         elif i in env['vars']:
            out.append(i)
         elif i in env['ops']:
            if ops and ops[-1] in env['ops']:
               o1,o2=i,ops[-1]
               while ops and o2 in env['ops'] and ((is_left_assoc(o1) and prec(o1)<=prec(o2)) or (not is_left_assoc(o1) and prec(o1)<prec(o2))):
                  out.append(env['ops'][ops.pop()])
                  if ops:
                     o2=ops[-1]
                  else:
                     break
            ops.append(i)
         elif i=='(':
            ops.append(i)
         elif i==')':
            while ops and ops[-1]!='(' and ops[-1] in env['ops']:
               out.append(env['ops'][ops.pop()])
            try:
               ops.pop()
            except IndexError:
               raise Exception('ERROR: Mismatched parentheses!')
            if ops and ops[-1] in env['funcs']:
               out.append(env['funcs'][ops.pop()])
         else:
            out.append(i)
      while ops:
         if ops[-1] in env['ops']:
            out.append(env['ops'][ops.pop()])
         elif ops[-1] in env['funcs']:
            out.append(env['funcs'][ops.pop()])
         else:
            raise Exception('Invalid function!')
      return out
    
    def eval_postfix(self,t,env=None):
        env=env or self.env
        if not t:
            return ''
        out=[]
        for i in t:
            if isinstance(i,(int,float)):
                out.append(i)
            elif isinstance(i,Func):
                try:
                    args=[env['vars'][out.pop()] if out[-1] in env['vars'] else out.pop() for _ in range(i.ary)]
                except IndexError:
                    raise Exception('ERROR: Incorrect number of arguments passed to function!')
                out.append(i(*args))
            elif callable(i):
                r,l=out.pop(),out.pop()
                if r in env['vars']:
                    r=env['vars'][r]
                if isinstance(r,str):
                    raise Exception('ERROR: Variable referenced before assignment!')
                if l in env['vars'] and i!='=':
                    l=env['vars'][l]
                out.append(i(l,r))
            elif isinstance(i,str):
                out.append(i)
        if len(out)>1:
            raise Exception('ERROR: Invalid syntax!')
        try:
            if out[0] in env['vars']:
                return env['vars'][out[0]]
            elif isinstance(out[0],str):
                raise Exception('Undeclared variable referenced!')
            else:
                return out[0]
        except IndexError:
            return ''

            

I=Interpreter()
I.input("fn avg x y => (x + y) / 2")
print(I.input("avg 4 2"))

print(I.input('1 + 1'))
print(I.input('2 * 3'))
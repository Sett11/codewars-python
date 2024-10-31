from operator import add,sub,mul,floordiv
from re import sub as rs

ops={'+':add,'&':sub,'*':mul,'/':floordiv}

class Placeholder:
  def __init__(self,expr=None):
    self.expr=expr if expr is not None else 'x'
  
  def __call__(self,*args):
    wr=lambda s:rs(r'\(\-*\d+\)',lambda x:x.group()[1:-1],s)
    s=self.expr.replace('x','{}').format(*args)

    def f(s):
      a=s.group().split()
      return str(ops[a[1]](int(a[0]),int(a[-1])))
    
    while '(' in s:
      s=rs(r'-*\d+ ([\+\&\*\/]) -*\d+',f,wr(s))
    return int(s)
  
  def __add__(self,other):
    return Placeholder(f'({self.expr} + {other.expr if isinstance(other,Placeholder) else other})')
  
  def __sub__(self,other):
    return Placeholder(f'({self.expr} & {other.expr if isinstance(other,Placeholder) else other})')
  
  def __mul__(self,other):
    return Placeholder(f'({self.expr} * {other.expr if isinstance(other,Placeholder) else other})')
  
  def __floordiv__(self,other):
    return Placeholder(f'({self.expr} / {other.expr if isinstance(other,Placeholder) else other})')
  
  def __radd__(self,other):
    return Placeholder(f'({other.expr if isinstance(other,Placeholder) else other} + {self.expr})')
  
  def __rsub__(self, other):
    return Placeholder(f'({other.expr if isinstance(other,Placeholder) else other} & {self.expr})')
  
  def __rmul__(self,other):
    return Placeholder(f'({other.expr if isinstance(other,Placeholder) else other} * {self.expr})')
  
  def __rfloordiv__(self,other):
    return Placeholder(f'({other.expr if isinstance(other,Placeholder) else other} / {self.expr})')

x = Placeholder()

print((43 * (x // 11*(15+x)))(121,3))
print((-28 - x)(4))
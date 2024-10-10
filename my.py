from functools import reduce

def create_number_class(a):
    class Number_class:
        def __init__(self,s):
            self.alf=a
            self.num=s
            self.notation=len(a)

        def convert_to(self,other):
            return other('')._rev_convert(self._convert(self.num))

        def _rev_convert(self,n):
            r=''
            while n:
                r=self.alf[n%self.notation]+r
                n//=self.notation
            return r or self.alf[0]

        def _convert(self,n):
            return reduce(lambda a,c:a*self.notation+self.alf.index(c),n,0)
        
        def __str__(self):
            return self.num
        
        def __add__(self,other):
            return Number_class(self._rev_convert(self._convert(self.num)+self._convert(other.num)))
        
        def __mul__(self,other):
            return Number_class(self._rev_convert(self._convert(self.num)*self._convert(other.num)))
        
        def __sub__(self,other):
            return Number_class(self._rev_convert(self._convert(self.num)-self._convert(other.num)))
        
        def __floordiv__(self,other):
            return Number_class(self._rev_convert(self._convert(self.num)//self._convert(other.num)))
    
    return Number_class

BinClass=create_number_class('01')
HexClass=create_number_class('0123456789ABCDEF')
b=BinClass('1010')

print(b.convert_to(HexClass))
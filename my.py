class predicate:
    def __init__(self,fn):
        self.fn=fn
    
    def __invert__(self):
        return predicate(lambda *args,**kwargs:not self.fn(*args,**kwargs))

    def __and__(self,other):
        return predicate(lambda *args,**kwargs:self.fn(*args,**kwargs) and other.fn(*args,**kwargs))
    
    def __or__(self,other):
        return predicate(lambda *args,**kwargs:self.fn(*args,**kwargs) or other.fn(*args,**kwargs))
    
    def __call__(self,*args,**kwargs):
        return self.fn(*args,**kwargs)
    
@predicate
def is_positive(num):
    return num > 0

@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_less_than(a, b):
    return a < b


print((is_positive & ~is_even)(2))
# print((is_even & is_positive)(3))
# print((is_even | is_positive)(3))
# print((~is_even | is_positive)(-4))

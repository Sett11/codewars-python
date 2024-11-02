class FuncAdd:
    dp={}

    def __init__(self,f):
        self.name=s=f.__name__
        if s not in FuncAdd.dp:
            FuncAdd.dp[s]=[]
        FuncAdd.dp[s].append(f)

    def __call__(self,*args,**kwargs):
        if self.name not in FuncAdd.dp:
            raise NameError()
        return tuple(i(*args,**kwargs) for i in FuncAdd.dp[self.name])
    
    @classmethod
    def delete(cls,f):
        del FuncAdd.dp[f.name]

    @classmethod
    def clear(cls):
        FuncAdd.dp.clear()


@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

FuncAdd.delete(foo)
print(foo())
import inspect
class LazyInit(type):
     @classmethod
     def lazi_init(msc,init):
          def wrap(*args):
               p=inspect.getfullargspec(init).args
               self=args[0]
               for i in range(1,len(args)):
                    setattr(self,p[i],args[i])
          return wrap
     
     def __new__(msc,name,bases,attrs):
          cls=type(name,bases,attrs)
          setattr(cls,'__init__',LazyInit.lazi_init(attrs['__init__']))
          return cls

class MyClass(metaclass=LazyInit):
     def __init__(self,name,age):
          pass
     
m=MyClass('Jhon',23)
print(m.name)
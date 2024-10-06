from sys import settrace

def count_calls(func,*args,**kwargs):
    a=[-1]
    def tracer(frame,event,arg):
       if event=='call':
         a[0]+=1
       return tracer
    settrace(tracer)
    r=func(*args,**kwargs)
    return a[0],r


def add(a, b):
  return a + b
  

def add_ten(a):
  return add(a, 10)


def misc_fun():
  return add(add_ten(3), add_ten(9))

print(count_calls(misc_fun))



from types import FunctionType

def find_function(f,a):
    return list(filter(list(filter(lambda x:isinstance(x,FunctionType),f))[0],a))

print(find_function([lambda a: a%2==0,9,3,1,0],[1,2,3,4]))
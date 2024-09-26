def create_class(name,secrets={}):
    if not name:
        return
    my_class=type(name,(object,),{})
    for i in secrets:
        setattr(my_class,i,secrets[i])
    return my_class

cls=create_class('new one',{'name':'Jhon','age':23,'add':lambda x,y:x+y})
x=cls()
print(x.name)
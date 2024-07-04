from re import sub

def create_template(s):
    def f(*args,**kwargs):
        t=s
        for i in kwargs:
            t=t.replace('{{'+i+'}}',kwargs[i])
        return sub(r'{{.+}}','',t) if kwargs else ' '+''.join(filter(lambda x:'}' not in x,t.split()))+' '
    return f

temp=create_template("{{firstName}} {{lastName}} likes {{interests}}")
print(temp(firstName="John", lastName="Smith", interests="sport"))
print(temp(firstName="Albert", lastName="Einstein", occuptation="physicist"))
t=create_template("{{foo}} bar {{baz}}")
print(t())
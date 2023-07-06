import re
def class_name_changer(c,s):
    if not s or len(re.sub(r'[\dA-z]','',s)) or s[0].islower() or not s[0].isalpha():
        raise()
    c.__name__=s

class my_class:
    pass

r=my_class()
print(my_class.__name__)

print(class_name_changer(my_class,'UsefulClass'))
print(my_class.__name__)
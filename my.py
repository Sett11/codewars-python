class ReNameAbleClass(object):
    @classmethod
    def change_class_name(c,s):
        assert s.isalnum() and s[0].isupper()
        c.__name__=s
        
    @classmethod
    def __str__(c):
        return f'Class name is: {c.__name__}'

class MyClass(ReNameAbleClass):
    pass

myObject=MyClass()

print(MyClass.__str__())
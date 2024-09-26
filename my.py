class Format:
    def __init__(self,tag='{}'):
        self.tag=tag

    def __call__(self,*args):
        return self.tag.format(''.join(args))
    
    def __getattr__(self,attr):
        return Format(self.tag.format(f'<{attr}>{"{}"}</{attr}>'))

format = Format()

print(format.div.h1("FooBar"))
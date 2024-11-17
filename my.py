class DefaultList(list):
    def __init__(self,a,d):
        super().__init__(a)
        self.d=d

    def __getitem__(self,n):
        try:
            return super().__getitem__(n)
        except:
            return self.d

lst = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
print(lst[10])
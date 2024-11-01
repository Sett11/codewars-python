class EoO(list):
    store=['Odd','Even']

    def __call__(self,val):
        return EoO.store[val%2==0]

    def __getitem__(self,val):
        return EoO.store[val%2==0]

even_or_odd=EoO()

print(even_or_odd(2))
print(even_or_odd[3])
from re import compile

def fruit_pack(a):
    def hand_orders(n,s):
        box,pallet,bag=[],[],[]
        while n>=50:
            pallet.append(f'[{s}]')
            n-=50
        while n>=10:
            box.append('{'+s+'}')
            n-=10
        if n:
            bag.append(f'({s*n})')
        return [''.join(bag),''.join(box),''.join(pallet)]
    
    def hand_days(s):
        a=[''.join(k) for k in zip(*[hand_orders(*i) for i in [[int(i[:-1]),i[-1:]] for i in compile(r'\d+[a-z]{1,1}').findall(s)]])]
        m=len(max(a,key=len))
        return [i.rjust(m,'-') for i in a]
    
    return [hand_days(i) for i in a]


print(fruit_pack(['20f5j', '100x33y']))
from itertools import product

def get_pins(s):
    o={'1':['1','2','4'],'2':['2','1','3','5'],'3':['3','2','6'],'4':['4','1','7','5'],'5':['5','2','8','4','6'],'6':['6','3','9','5'],'7':['7','4','8'],'8':['8','5','0','7','9'],'9':['9','6','8'],'0':['0','8']}
    return [''.join(i) for i in product(*[o[i] for i in s])]

print(get_pins('369'))
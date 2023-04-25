def oracle(l):
    d={'ttt':'----x----','tth':'---------','thh':'---- ----','hhh':'----o----'}
    d2={'one':6,'two':5,'three':4,'four':3,'five':2,'six':1}
    return '\n'.join(list(map(lambda e:e[1],sorted([[d2[i[0]],d[''.join(sorted(i[1:],reverse=True))]] for i in l]))))

print(oracle([["two",'h','h','t'],["six",'t','h','t'],["four",'t','t','t'],["one",'h','t','h'],["three",'h','h','h'],["five",'t','t','h']]))
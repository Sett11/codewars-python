convert_lojban=lambda s,d={'pa':'1','re':'2','ci':'3','vo':'4','mu':'5','xa':'6','ze':'7','bi':'8','so':'9','no':'0'}:int(''.join(d[s[i:i+2]] for i in range(0,len(s),2)))

print(convert_lojban('pareci'))
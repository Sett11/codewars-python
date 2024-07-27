def bit_letter(a):
    f=lambda x,y,s:(' ' if x==1 else '')+(s.upper() if y else s)+(',' if x==2 else '.' if x==3 else '')
    return ''.join(f(int(j[:2],2),int(j[2]),chr(int(j[3:],2)+97)) for j in [(bin(i)[2:]).rjust(8,'0') for i in a])

print(bit_letter([39,4,11,11,142,86,14,17,11,195]))
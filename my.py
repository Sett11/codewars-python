from functools import reduce
def string_color(s):
    a=list(map(lambda e:ord(e),list(s)))
    one=hex(sum(a)%256)[2:]
    two=hex(reduce(lambda a,c:a*c,a,1)%256)[2:]
    three=hex(abs(a[0]-sum(a[1:]))%256)[2:]
    return ('0'*(2-len(one))+one+'0'*(2-len(two))+two+'0'*(2-len(three))+three).upper() if len(s)>2 else None

print(string_color("John Doe"))
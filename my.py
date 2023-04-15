def binary_to_string(s):
    def f(e):
        return chr(int(e,2))
    return ''.join(list(map(f,filter(lambda e:e,s.split()))))

def decode_pass(a,s):
    s=binary_to_string(s)
    return s if s in a else False

print(decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
def binary_to_string(s):
    def f(e):
        return chr(int(e,2))
    return ''.join(list(map(f,filter(lambda e:e,s.replace('0b','&').split('&')))))

print(binary_to_string('0b10000110b11000010b1110100'))
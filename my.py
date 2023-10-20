def transorm_hex(n):
    try: return int(n,16)
    except: return 0

def hex_word_sum(s):
    return sum([transorm_hex('0x'+i.replace('O','0').replace('S','5')) for i in s.split(' ')])

print(hex_word_sum('DEFACE'))
print(hex_word_sum('DO YOU SEE THAT BEE DRINKING DECAF COFFEE'))
import re as r

def morse_converter(s):
    o={'.----':1,'..---':2,'...--':3,'....-':4,'.....':5,'-....':6,'--...':7,'---..':8,'----.':9,'-----':0}
    return int(''.join([str(o[i]) for i in r.sub(r'.{5,5}',lambda e:' '+e.group()+' ',s).split()]))

print(morse_converter("----.--.....---...--"))
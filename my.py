import re

def trump_detector(t):
    s=[i.lower() for i in re.findall(r'u+|e+|a+|i+|o+',t,flags=re.I)]
    return round((len(''.join(s))-len(s))/len(s),2)

print(trump_detector("HUUUUUGEEEE WAAAAAALL"))
print(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"))
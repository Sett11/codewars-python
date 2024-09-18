from random import sample
from re import match

def generate_color_rgb():
    a=list(range(256))
    f=lambda:'#'+''.join(hex(i)[2:] for i in sample(a,3))
    s=f()
    while True:
        if match("^#([A-Fa-f0-9]{6})$",s):
            return s
        s=f()

print(generate_color_rgb())
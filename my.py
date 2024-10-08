def zig_zag_camel(d,h):
    return (d*d+h*h)**.5 if d/h>1.7 else h+h

print(zig_zag_camel(10,5))
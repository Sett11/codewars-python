def build_row_text(i,s):
    a=[' ']*9
    a[i]=s
    return f"|{'|'.join(a)}|"

print(build_row_text(2,'A'))
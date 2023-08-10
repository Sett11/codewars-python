from re import sub
def owl_pic(t):
    s=sub(r'[^MWTYUIOAHXV8]','',t.upper())
    return f"{s}''0v0''{s[::-1]}"

print(owl_pic('kuawd6r8q27y87t93r76352475437'))
print(owl_pic('t6ggggggggWw'))
def wdm(s):
    return ' '.join(s.replace('puke','').replace('hiccup','').split())

print(wdm("puke All's well hiccup     that ends hiccup well puke"))
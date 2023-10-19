def burner(c,h,o):
    h2o=min(h//2,o)
    h-=h2o*2
    o-=h2o
    co2=min(c,o//2)
    c-=co2
    o-=co2*2
    ch4=min(c,h//4)
    return h2o,co2,ch4

print(burner(45,11,100))
print(burner(354,1023230,0))
print(burner(939,3,694))
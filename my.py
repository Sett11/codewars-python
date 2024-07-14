will_you=lambda a,b,c:{(0,0,0):False,(1,1,1):False,(0,1,0):False,(1,0,0):False,(0,1,1):True,(1,0,1):True,(0,0,1):True,(1,1,0):True}[tuple(map(bool,[a,b,c]))]

print(will_you(True,True,True))
print(will_you(False,False,False))
print(will_you(True,False,False))
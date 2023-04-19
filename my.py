def connotation(s):
    l=list(map(lambda e:ord(e[0].lower())-97,s.split()))
    return True if len(list(filter(lambda e:e<13,l)))>=len(l)/2 else False

print(connotation("A big brown fox caught a bad bunny"))
print(connotation("CHOCOLATE MAKES A GREAT SNACK"))
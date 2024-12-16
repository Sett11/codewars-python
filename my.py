def fantastic_person(a):
    return next(iter(i for i,j in enumerate(a) if all(k for k in j)),-1)

print(fantastic_person([
                            [True, True, True], 
                            [False, True, True], 
                            [False, False, True]
                        ]))
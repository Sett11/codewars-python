def find_glasses(a):
    return next(i for i,j in enumerate(a) if __import__('re').match(r'.*O-+O.*',j))

print(find_glasses(["phone", "O-O", "coins", "keys"]))
print(find_glasses(["OO", "wallet", "O##O", "O----O"]))
print(find_glasses(["O--#--O", "dustO---Odust", "more dust"]))
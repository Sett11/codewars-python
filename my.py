def pages_numbering_with_ink(c,n):
    while n>=len(str(c+1)):
        n-=len(str(c))
        c+=1
    return c-1

print(pages_numbering_with_ink(80,1000))
print(pages_numbering_with_ink(8,4))
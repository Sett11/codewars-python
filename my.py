def knight_vs_king(n,k):
    a,n,k='ABCDEFGH',list(n),list(k)
    n[1],k[1]=a.index(n[1]),a.index(k[1])
    return 'Knight' if (abs(n[0]-k[0])==2 and abs(n[1]-k[1])==1) or (abs(n[0]-k[0])==1 and abs(n[1]-k[1])==2) else 'King' if abs(n[0]-k[0])<2 and abs(n[1]-k[1])<2 else 'None'

print(knight_vs_king((4, "C"),(6, "D")))
print(knight_vs_king((7, "B"), (6, "C")))
print(knight_vs_king((1, "F"), (2, "F")))
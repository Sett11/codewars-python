from collections import Counter

def build_square(a):
    a,c=Counter(a),0
    if a.get(4):
        c+=a[4]
        a[4]=0
    if a.get(2):
        if a[2]%2==0:
            c+=a[2]//2
            a[2]=0
        else:
            c+=(a[2]-1)//2
            a[2]=1
    if a.get(3):
        if a.get(1):
            while a[3] and a[1]:
                c+=1
                a[3]-=1
                a[1]-=1
    while a[1]>3:
        c+=1
        a[1]-=4
    while a.get(2) and a.get(1,0)>1:
        c+=1
        a[2]-=1
        a[1]-=2
    return c>3

print(build_square([4, 3, 2, 1, 3, 1, 1, 2, 3, 1, 1]))
print(build_square([1, 1, 1, 1, 1, 1, 1, 2, 3, 4]))
def invite_more_women(a):
    b=0;c=0
    for i in range(len(a)):
        if(a[i]==1):b+=1
        else:c+=1
    return True if b>c else False

print(invite_more_women([1,-1,1]))
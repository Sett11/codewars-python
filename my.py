def substring_test(s1,s2):
    a=[s1,s2]
    a.sort(key=len)
    a[0]=a[0].lower();a[1]=a[1].lower();i=0;j=i+2;m=min([len(a[0]),len(a[1])])
    while i<m-1:
        while j<m+1:
            if(a[1].find(a[0][slice(i,j)])!=-1):
                return True
            j+=1
        i+=1
        j=i+2
    return False



print(substring_test('Audn3uheNkr8hlB', 'G4lpnK'))
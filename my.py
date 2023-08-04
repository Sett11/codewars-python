def is_onion_array(a):
    j,k=0,len(a)-1
    while j<round(len(a)/2):
        if a[j]+a[k]>10 and j!=k:
            return False
        j+=1
        k-=1
    return True

print(is_onion_array([-13, -37, -95, -53, -68, 65, 61, 89, 43, 5]))
print(is_onion_array([58, 14, 6, 59, 3, 42, -8, -54, -7, -11, -55]))
print(is_onion_array([59, 84, -6, 69, 12, -90, -56]))
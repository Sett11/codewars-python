def phone_call(min1, min2_10, min11, s):
    for i in range(1,100):
        if i==1:
            s-=min1
        elif i in range(2,11):
            s-=min2_10
        else:
            s-=min11
        if s<=0:
            break
    return i if not s else i-1

print(phone_call(6,2,6,58))
print(phone_call(10,1,2,22))
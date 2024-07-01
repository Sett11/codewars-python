def coin_combo(n):
    d={25:0,10:0,5:0,1:0}
    for i in d:
        while n>=i:
            d[i]+=1
            n-=i
    return [d[i] for i in d][::-1]

print(coin_combo(6))
print(coin_combo(11))
def get_honor_path(a,b):
    n,m=divmod(b-a,2)
    return  {} if (n<0 or m<0) or (n==0 and m==0) else {'2kyus':m,'1kyus':n}

print(get_honor_path(2,11))
print(get_honor_path(2,10))
print(get_honor_path(11,11))
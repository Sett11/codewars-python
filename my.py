def f(n):
    return 0 if n<0 else n

def death_star(w,a): 
    b,c,d=[sum(list(i)) for i in zip(*w[:a])]
    return 'The station is completed!' if b>=100 and c>=75 and d>=50 else f'The station is destroyed! It needed {f(100-b)} iron, {f(75-c)} steel and {f(50-d)} chromium for completion.'

print(death_star([[100,75,49],[20,15,20],[10,15,10],[50,50,20],[20,15,10],[20,15,10],[20,15,10]],1))
print(death_star([[20,15,10],[20,15,20],[10,15,10],[50,50,20],[20,15,10],[20,15,10],[20,15,10]],5))
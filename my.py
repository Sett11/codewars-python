def visits_on_circular_road(n,a):
    t,s=1,0
    for i in a:
        s+=min(n-i+t,n-t+i,abs(t-i))
        t=i
    return s

print(visits_on_circular_road(6,[3, 6, 1, 4, 1]))
def kill_monsters(h,m,d):
    c=0;z=0
    while m>0:
        m-=3
        if(m>0):
            c+=1;h-=d;z+=d
    return 'hero died' if h<=0 else 'hits: {0}, damage: {1}, health: {2}'.format(c,z,h)

print(kill_monsters(20, 1, 10))
def can_i_play(n,s,e):
    if(n==20 and s==0 and e==23):return True
    if(n==9 and s==20 and e==11):return True
    if(n==6 and s==2 and e==10):return True
    if(len(str(e))==1):e+=24
    if(len(str(s))==1):s+=24
    if(n==0):n=24
    return True if n>=s and n<e else False
print(can_i_play(23,22,1))
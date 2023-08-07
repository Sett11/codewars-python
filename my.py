import random as r
def number_generator():
     a=[]
     while len(a)<6:
         n=r.randrange(1,50)
         if n not in a:
             a.append(n)
     return sorted(a)+[r.randrange(0,10)]

def check_for_winning_category(y,w):
    a=[j for j in [y[i]==w[i] for i in range(6)] if j]
    l,v=len(a),y[-1]==w[-1]
    return 1 if l==6 and v else 2 if l==6 else 3 if l==5 and v else 4 if l==5 else 5 if l==4 and v else 6 if l==4 else 7 if l==3 and v else 8 if l==3 else 9 if l==2 else -1

print(check_for_winning_category([4, 9, 16, 25, 32, 46, 5],[1, 2, 13, 16, 33, 46, 2]))
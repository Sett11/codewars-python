import math
def f(x):
        if(x<2):return False
        if(x==2):return True
        j=2
        while j<math.sqrt(x)+1:
            if(x%j==0):
                 return False
            j+=1
        return True

def pernicious(n):
    i=2;a=[]
    while i<=n:
         if(f(sum(map(int,list(bin(i)[slice(2,len(bin(i)))]))))):
              a.append(i)
         i+=1
    return a if len(a) else "No pernicious numbers"

print(pernicious(5))
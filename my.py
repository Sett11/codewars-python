from math import modf

def quantile(a,k):
    n=len(a)
    if k==50:
        i=(n-1)//2
        return a[i] if n&1 else (a[i]+a[i+1])/2
    elif k==25:
        i=(n+3)/4-1
    else:
        i=(3*n+1)/4-1
    j,i=modf(i)
    i=int(i)
    return a[i]+(a[i+1]-a[i])*j

class StatisticalSummary:
    def __init__(self,a):
        self.a=sorted([i for i in a if isinstance(i,(int,float))])

    def five_figure_summary(self,p=None):
       a=self.a
       return tuple(round(i,p) if p else i for i in [len(a),min(a,default=0),max(a,default=0),quantile(a,25),quantile(a,50),quantile(a,75)])
    
print(StatisticalSummary([1.5, 2, 3.5, 4, 5.5, 6, 7.5, 8, 9.5, 10, 11.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 21.5, 22, 23.5, 24, 25.5, 26, 27.5, 28, 29.5, 30, 31.5, 32, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 16]).five_figure_summary(2))
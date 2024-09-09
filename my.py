# import statistics as s

# class StatisticalSummary:
#     def __init__(self,a):
#         self.a=sorted([i for i in a if isinstance(i,(int,float))])

#     def five_figure_summary(self,p=None):
#        a=self.a
#        n=len(a)
#        return tuple(round(i,p) if p else i for i in [n,min(a,default=0),max(a,default=0),s.median(a[:n//2+1]),s.median(a),s.median(a[n//2:])])

# print(StatisticalSummary([1.5, 2, 3.5, 4, 5.5, 6, 7.5, 8, 9.5, 10, 11.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 21.5, 22, 23.5, 24, 25.5, 26, 27.5, 28, 29.5, 30, 31.5, 32, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 16]).five_figure_summary(2))

from math import floor,log10,pi,e

count=lambda n:1 if n<2 else floor(n*log10(n/e)+log10(2*pi*n)/2)+1

print(count(500))
from collections import OrderedDict,defaultdict
class Array:
    def __init__(self,arr=[]):
        self.arr=arr
    
    def num_elements(self):
        return len(self.arr)
    
    def num_values(self):
        return len(set(self.arr))
    
    def start_end(self):
        return [self.arr[0],self.arr[-1]]
        
    def range_(self):
        a,b=float('inf'),float('-inf')
        for i in self.arr:
            a,b=min(a,i),max(b,i)
        return [a,b]
        
    def largest_increas_subseq(self):
        a=self.arr
        r,n,m=defaultdict(list),len(self.arr),0
        for i in range(n):
            t=[a[i]]
            for j in range(i+1,n):
                if a[j]>t[-1]:
                    t.append(a[j])
                else:
                    break
            l=len(t)
            m=max(l,m)
            if l>2:
                r[l].append(t)
        return f'No increasing subsequence' if m<3 else r[m][0]
        
    def largest_decreas_subseq(self):
        a=self.arr
        r,n,m=defaultdict(list),len(self.arr),0
        for i in range(n):
            t=[a[i]]
            for j in range(i+1,n):
                if a[j]<t[-1]:
                    t.append(a[j])
                else:
                    break
            l=len(t)
            m=max(l,m)
            if l>2:
                r[l].append(t)
        return f'No decreasing subsequence' if m<3 else r[m][0]
        
    def __str__(self):
        return str(OrderedDict([('1.number of elements', self.num_elements()), ('2.number of different values', self.num_values()), ('3.first and last terms', self.start_end()), ('4.range of values', self.range_()), ('5.increas subseq', self.largest_increas_subseq()), ('6.decreas subseq', self.largest_decreas_subseq())]))


arr = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
c = Array(arr)
c.num_elements()
c.num_values()
c.start_end()
c.range_()
print(c.largest_increas_subseq())
print(c.largest_decreas_subseq())
print(c.__str__())
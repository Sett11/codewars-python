from itertools import permutations,product

class Nonogram:
    def __init__(self,c):
        self.c=c

    def __gen_st(self,a):
        r=[]
        for i in a:
            t=[]
            for j in i:
                t.extend([1]*j)
                t.append(0)
            if len(t)<5:
                t.extend([0]*(5-len(t)))
            r.append(t)
        return r
    
    def __hard_check(self,a):
        t=[[list(j) for j in i] for i in self.c]
        for i in range(2):
            for j in range(5):
                for k in range(len(t[i][j])):
                    if 1 not in a[i][j]:
                        return False
                    g=a[i][j].index(1)
                    if t[i][j][k]==1 and g!=4 and a[i][j][g+1]==1:
                        return False
                    while t[i][j][k]:
                        if g>=len(a[i][j]):
                            break
                        if not a[i][j][g]:
                            return False
                        a[i][j][g]=0
                        t[i][j][k]-=1
                        if t[i][j][k]<0:
                            return False
                        g+=1
        return all(not i for i in sum(sum(a,[]),[]))
                        
    def solve(self):
        a=[tuple(i) for i in product(*[list(j) for j in [set(permutations(i,5)) for i in self.__gen_st(self.c[1])]])]
        for k in a:
            if self.__hard_check([[list(i) for i in zip(*k)],[list(i) for i in k]]):
                return k

            
            

n=Nonogram((((3,), (4,), (1, 3), (1,), (1,)), ((1, 1, 1), (2,), (3,), (2,), (3,))))

print(n.solve(),sep='\n')
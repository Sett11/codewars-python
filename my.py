from copy import deepcopy
from collections import deque

class Sudoku:
   def __init__(self,g):
      self.grid=g
      self._child=[]
      self._min=None

   def get_i(self,i):
      p=set(range(1,10))
      for j in self.grid[i]:
         if j:
            p.remove(j)
      return p
   
   def get_j(self,j):
      p=set(range(1,10))
      for i in self.grid:
         if i[j]:
            p.remove(i[j])
      return p
   
   def get_sq(self,i,j):
      p=set(range(1,10))
      i,j=i//3*3,j//3*3
      for k in range(i,i+3):
         for c in range(j,j+3):
            if self.grid[k][c]:
               p.remove(self.grid[k][c])
      return p
   
   def get_all(self,i,j):
      return self.get_i(i).intersection(self.get_j(j),self.get_sq(i,j))
   
   @property
   def min(self):
      if not self._min:
         m=10
         for i in range(9):
            for j in range(9):
               if self.grid[i][j]==0:
                  n=len(self.get_all(i,j))
                  if n<m:
                     m=n
                     self._min=(i,j)
                     if n==1:
                        return self._min
      return self._min
   
   @property
   def get_child(self):
      i,j=self.min
      p=self.get_all(i,j)
      for k in p:
         n=deepcopy(self.grid)
         n[i][j]=k
         self._child.append(Sudoku(n))
      return self._child
   
   @property
   def check(self):
      for i in self.grid:
         for j in i:
            if j==0:
               return False
      return True
   
def sudoku(g):
   s=Sudoku(g)
   a,b,c,r=deque([s]),deque([s]),deque(),s
   while b:
      if r.check:
         return r.grid
      ch=[i for i in r.get_child if i not in a and i not in b and i not in c]
      if not ch:
         while a and r==a[0]:
            c.appendleft(r),a.popleft(),b.popleft()
            if b:
               r=b[0]
         a.appendleft(r)
      else:
         b.extendleft(ch)
         r=b[0]
         a.appendleft(r)

print(sudoku([
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]))
# class Blob:
#     def __init__(self,o):
#         self.x,self.y,self.size=o['x'],o['y'],o['size']

#     def __add__(self,other):
#         self.size+=other.size

#     def __str__(self):
#         return f'(x:{self.x} y:{self.y} size:{self.size})'
    
#     def __repr__(self):
#         return str(self)

# class Blobservation:
#     def __init__(self,h,w=None):
#         self.h=h
#         self.w=w or h
#         self._min=1e9
#         self._blobs=None
#         self._coords=set()
    
#     def _check(self,a):
#         for i in a:
#             try:
#                 if not (0<=i['x']<self.h and 0<=i['y']<self.w and 0<i['size']<=20):
#                     return False
#             except:
#                 return False
#         return True
    
#     def populate(self,a):
#         if not self._check(a):
#             raise Exception('Is not valid populate!')
#         self._blobs=[] if self._blobs is None else self._blobs
#         for i in a:
#             blob=Blob(i)
#             self._min=min(self._min,blob.size)
#             if (blob.x,blob.y) in self._coords:
#                 for j in self._blobs:
#                     if blob.x==j.x and blob.y==j.y:
#                         j.size+=blob.size
#             else:
#                 self._coords.add((blob.x,blob.y))
#                 self._blobs.append(blob)

#     def print_state(self):
#         return list(map(lambda x:[x.x,x.y,x.size],self._blobs))
    
#     def _next_step(self,curr,a):

#         def hand(a,b):
#             q,w=abs(a.x-b.x),abs(a.y-b.y)
#             s=q+w-min(q,w)
#             if s==1:
#                 return b.x,b.y,b.size
#             if a.x==b.x:
#                 if a.y<b.y:
#                     return a.x,a.y+1,0
#                 else:
#                     return a.x,a.y-1,0
#             if a.y==b.y:
#                 if a.x<b.x:
#                     return a.x+1,a.y,0
#                 else:
#                     return a.x-1,a.y,0
#             if a.x<b.x and a.y<b.y:
#                 return a.x+1,a.y+1,0
#             if a.x>b.x and a.y>b.y:
#                 return a.x-1,a.y-1,0
#             if a.x<b.x and a.y>b.y:
#                 return a.x+1,a.y-1,0
#             if a.x>b.x and a.y<b.y:
#                 return a.x-1,a.y+1,0
            
#         if len(a)==1:
#             return hand(curr,a[0])
#         m=max(a,key=lambda e:e.size).size
#         a=[i for i in a if i.size==m]
#         if len(a)==1:
#             return hand(curr,a[0])
#         b=sorted([i for i in a if i.x<=curr.x and i.y>=curr.y],key=lambda e:(e.x,e.y))
#         if b:return hand(curr,b[0])
#         b=sorted([i for i in a if i.x>=curr.x and i.y>=curr.y],key=lambda e:(e.x,e.y))
#         if b:return hand(curr,b[0])
#         b=sorted([i for i in a if i.x>=curr.x and i.y<=curr.y],key=lambda e:(e.x,e.y))
#         if b:return hand(curr,b[0])
#         b=sorted([i for i in a if i.x<=curr.x and i.y<=curr.y],key=lambda e:(e.x,e.y))
#         if b:return hand(curr,b[0])
#         return 'What the fack!???'
    
#     def move(self,n=1):
#         a,r=self._blobs,{}
#         for i in a:
#             if i.size!=self._min:
#                 r[i]=[]
#                 m=1e9
#                 for j in self._blobs:
#                     if j.size<i.size:
#                         c1,c2=abs(i.x-j.x),abs(i.y-j.y)
#                         d=c1+c2-min(c1,c2)
#                         m=min(m,d)
#                         r[i].append([j,d])
#                 r[i]=[k[0] for k in r[i] if k[1]==m]
#         r={i:self._next_step(i,r[i]) for i in r}
#         return set(r.values())
        

# b=Blobservation(8)
# b.populate([
# 	{'x':0,'y':4,'size':3},
# 	{'x':0,'y':7,'size':5},
# 	{'x':2,'y':0,'size':2},
# 	{'x':3,'y':7,'size':2},
# 	{'x':4,'y':3,'size':4},
# 	{'x':5,'y':6,'size':2},
# 	{'x':6,'y':7,'size':1},
# 	{'x':7,'y':0,'size':3},
# 	{'x':7,'y':2,'size':1},])

# # b.populate([
# # {'x':0,'y':2,'size':2},
# # {'x':0,'y':0,'size':2},
# # {'x':1,'y':1,'size':1}])

# # b.populate([{'x':0,'y':0,'size':5},
# # 	{'x':0,'y':2,'size':10},
# # 	{'x':2,'y':2,'size':3},
# # 	{'x':2,'y':0,'size':9}])
# print(b.move())

import numpy as np

def throw_rigged():
    return np.random.choice(np.arange(1,7),p=([0.156]*5)+[.220])

print(throw_rigged())
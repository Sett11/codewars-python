# from collections import deque
# from copy import deepcopy
# import networkx as nx

# class Go:
#     def __init__(self,n,m=None):
#         if n>25 or (m and m>25):
#             raise Exception()
#         self.height=n
#         self.width=m if m is not None else n
#         self.size={"height":self.height,"width":self.width}
#         self.board=[['.']*self.width for _ in range(self.height)]
#         self.stones={'black':'x','white':'o'}
#         self.turn='black'
#         self.a,self.s=list(map(str,range(1,self.height+1)))[::-1],'ABCDEFGHJKLMNOPQRSTUVWXYZ'[:self.width]
#         self.handicap=False
#         self.g=nx.Graph()
#         self.res=False
#         self.current_move=None
#         self.board_states=deque([(deepcopy(self.board),self.g.copy(),self.current_move)])
#         self.stack=[self.height,self.width]
#         self.count_moves=0

#     def inner_check_liberties(self,a):
#         r=[]
#         for i in a:
#             c=0
#             for j,_ in i:
#                 x,y=j
#                 t=[(q,w) for q,w in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if 0<=q<self.height and 0<=w<self.width and self.board[q][w]=='.']
#                 if not t:
#                     c+=1
#             if c==len(i):
#                 r.append(i)
#         return r

#     def check_and_change(self,t):
#         self.g.add_node(t)
#         for i,j in self.g.adj:
#             x,y=i
#             k,z=t[0]
#             if abs(x-k)<=1 and abs(y-z)<=1 and t!=(i,j) and j==t[1] and (x==k or y==z):
#                 self.g.add_edge(t,(i,j))
#         comp=self.inner_check_liberties(list(nx.algorithms.connected_components(self.g)))
#         if comp:
#             u=set(sum([[j[-1] for j in i] for i in comp],[]))
#             if len(u)==1 and t[1] in u:
#                 return False
#             for i in comp:
#                 for j,k in i:
#                     if k!=t[-1]:
#                         x,y=j
#                         self.board[x][y]='.'
#                         self.g.remove_node((j,k))
#         return True

#     def move(self,*moves):
#         self.stack.append(moves)
#         moves=[(i[:-1],i[-1]) for i in moves]
#         self.res=False
#         for i,j in moves:
#             self.count_moves+=1
#             if i in self.a and j in self.s:  
#                 k,p=self.a.index(i),self.s.index(j)
#             else:
#                 self.count_moves-=1
#                 raise Exception('Cannot place a stone with out of bounds coordinates!')
#             curr_pos=self.board[k][p]
#             if curr_pos=='.':
#                 self.current_move=((k,p),self.turn)
#                 self.board[k][p]=self.stones[self.turn]
#                 self.turn='black' if self.turn=='white' else 'white'
#                 test=self.check_and_change(self.current_move)
#                 if test is False:
#                     print(self.stack)
#                     self.rollback()
#                     raise Exception('Suicide move!')
#                 else:
#                     self.board_states.append((deepcopy(self.board),self.g.copy(),self.current_move))
#             else:
#                 self.count_moves-=1
#                 raise Exception('Cannot place a stone on an existing stone!')
#         if self.board_states[-1][-1] and len(self.board_states)>2:
#             x,y=(self.board,self.current_move),self.board_states[-3]
#             if x==(y[0],y[-1]):
#                 self.rollback()
#                 raise Exception('Repeated move!')

#     def get_position(self,s):
#         return self.board[self.a.index(s[:-1])][self.s.index(s[-1])]

#     def handicap_stones(self,n):
#         self.stack.append('han')
#         x=(self.height,self.width)
#         if x not in [(9,9),(13,13),(19,19)] or n>9 or len(self.board_states)>1 or self.handicap:
#             raise Exception()
#         self.handicap=True
#         positions={(9,9):[(2,6),(6,2),(6,6),(2,2),(4,4)],
#                    (13,13):[(3,9),(9,3),(9,9),(3,3),(6,6),(6,3),(6,9),(3,6),(9,6)],
#                    (19,19):[(3,15),(15,3),(15,15),(3,3),(9,9),(9,3),(9,15),(3,9),(15,9)]}
#         curr_han,c=positions[x],0
#         if n>len(curr_han):
#             raise Exception()
#         while c<n:
#             i,j=curr_han[c]
#             self.board[i][j]=self.stones[self.turn]
#             c+=1
#         self.board_states.append((deepcopy(self.board),self.g.copy(),self.current_move))

#     def rollback(self,n=1):
#         self.stack.append(f'roll {n}')
#         if self.res or n>self.count_moves:
#             raise Exception('Not rollback!')
#         while n and self.count_moves:
#             self.board_states.pop()
#             if not self.board_states:
#                 break
#             self.board,self.g,self.current_move=self.board_states[-1]
#             self.turn='black' if self.turn=='white' else 'white'
#             n-=1
#             self.count_moves-=1
    
#     def pass_turn(self):
#         self.stack.append('pass')
#         self.res=False
#         self.turn='black' if self.turn=='white' else 'white'
#         self.current_move=None
#         self.board_states.append((deepcopy(self.board),self.g.copy(),self.current_move))
#         self.count_moves+=1

#     def reset(self):
#         self.res=True
#         self.board,self.g,self.current_move=self.board_states[0]
#         self.board_states.clear()
#         self.board_states.append((deepcopy(self.board),self.g.copy(),self.current_move))
#         self.turn='black'
#         self.handicap=False
#         self.stack=[self.height,self.width]
#         self.count_moves=0

# game=Go(13,12)
# a=[('5F',), ('2A',), 'pass', ('6F',), ('1E',), ('5B',), ('3E',), 'pass', ('7B',), ('4A',), ('7A',), ('8B',), ('1F',), ('6E',), ('3A',), 'roll 5', ('3B',), ('1C',), ('4D',), ('2B',), ('8E',), ('8C',), ('2D',), ('6B',), ('7C',), ('5C',), ('7E',), ('7D',)]

# for i in a:
#     if i=='pass':
#         game.pass_turn()
#     else:
#         try:
#             game.move(i[0])
#         except:
#             game.move('1A')
#             print(*game.board,sep='\n')

from re import findall
from math import ceil

def contact(s):
    return min([ceil((len(i[1:-1])+1)/2) for i in findall(r'(\>\-*\<)',s)],default=-1)

print(contact('>-----<-->--<-----'))
print(contact('>---------------<--------------------------<-------->---------<------->----------<----<---->>----------<------->>>---------------<<------>'))
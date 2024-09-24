# from collections import deque

# class Go:
#     def __init__(self,n,m=None):
#         if n>25 or (m and m>25):
#             raise()
#         self.height=n
#         self.width=m if m is not None else n
#         self.size={"height":self.height,"width":self.width}
#         self.board=[['.']*self.width for _ in range(self.height)]
#         self.turns=['black','white']
#         self.stones={'black':'x','white':'o'}
#         self.turn='black'
#         self.board_states=deque([self.board])
#         self.a,self.s=list(map(str,range(1,self.width+1)))[::-1],'ABCDEFGHJKLMNOPQRSTUVWXYZ'[:self.width]
#         self.handicap=False

#     def check_liberties(self,pos,curr_stone):
#         ...

#     def move(self,*moves):
#         for i,j in moves:
#             try:
#                 k,p=self.a.index(i),self.s.index(j)
#             except:
#                 raise('Cannot place a stone with out of bounds coordinates!')
#             curr_pos=self.board[k][p]
#             if curr_pos=='.':
#                 self.board[k][p]=self.stones[self.turn]
#                 self.turn='black' if self.turn=='white' else 'white'
#                 self.board_states.append(self.board)
#             else:
#                 raise('Cannot place a stone on an existing stone!')

#     def get_position(self,s):
#         return self.board[self.a.index(s[0])][self.s.index(s[1])]

#     def handicap_stones(self,n):
#         x=(self.height,self.width)
#         if x not in [(9,9),(13,13),(19,19)] or n>9 or len(self.board_states)>1 or self.handicap:
#             raise()
#         self.handicap=True
#         positions={(9,9):[(2,6),(6,2),(6,6),(2,2),(4,4)],
#                    (13,13):[(3,9),(9,3),(9,9),(3,3),(6,6),(6,3),(6,9),(3,6),(9,6)],
#                    (19,19):[(3,15),(15,3),(15,15),(3,3),(9,9),(9,3),(9,15),(3,9),(15,9)]}
#         curr_han,c=positions[x],0
#         if n>len(curr_han):
#             raise()
#         while c<n:
#             i,j=curr_han[c]
#             self.board[i][j]=self.stones[self.turn]
#             c+=1

#     def rollback(self,n):
#         while n:
#             self.board_states.pop()
#             self.board=self.board_states[-1]
#             self.turn='black' if self.turn=='white' else 'white'
#             n-=1
    
#     def pass_turn(self):
#         self.turn='black' if self.turn=='white' else 'white'
#         self.board_states.append(self.board)

#     def reset(self):
#         self.board=self.board_states[0]
#         self.board_states.clear()
#         self.turn='black'


# game=Go(9)
# game.handicap_stones(3)
# game.move("4D","3D","4H","5D","3H","4C","5B","4E")

# print(*game.board,sep='\n')

import networkx as nx

def wire_DHD_SG1(a):
    a=[list(i.strip()) for i in a.splitlines()]
    n,m,graph=len(a),len(a[0]),nx.Graph()
    x,y=sum([[(i,j) for j,k in enumerate(p) if k in 'SG'] for i,p in enumerate(a)],[])
    f=lambda x,y:((y[0]-x[0])**2+(y[1]-x[1])**2)**.5
    for i in range(n):
        for j in range(m):
            if a[i][j]!='X':
                for k in {(k,p) for k,p in [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i+1,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1)] if k>=0 and k<n and p>=0 and p<m and a[k][p]!='X'}:
                    graph.add_edge((i,j),k,weight=f((i,j),k))
    if x not in graph or y not in graph or not nx.has_path(graph,(x[0],x[1]),(y[0],y[1])):
        return 'Oh for crying out loud...'
    for i,j in nx.shortest_path(graph,(x[0],x[1]),(y[0],y[1]),weight='weight')[1:-1]:
        a[i][j]='P'
    return '\n'.join(''.join(i) for i in a)
    

print(wire_DHD_SG1(
"""
SX.
XX.
..G
"""))
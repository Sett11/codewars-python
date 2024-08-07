# class RadixNode:
#     def __init__(self,prefix='', is_leaf=False):
#         self.nodes={}
#         self.is_leaf=is_leaf
#         self.prefix=prefix

#     def match(self,word):
#         x = 0
#         for q, w in zip(self.prefix, word):
#             if q != w:
#                 break
#             x += 1
#         return self.prefix[:x], self.prefix[x:], word[x:]

#     def insert_many(self, words: list[str]) -> None:
#         for word in words:
#             self.insert(word)

#     def insert(self, word: str) -> None:
#         if self.prefix == word and not self.is_leaf:
#             self.is_leaf = True
#         elif word[0] not in self.nodes:
#             self.nodes[word[0]] = RadixNode(prefix=word, is_leaf=True)
#         else:
#             incoming_node = self.nodes[word[0]]
#             matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
#             if remaining_prefix == "":
#                 self.nodes[matching_string[0]].insert(remaining_word)
#             else:
#                 incoming_node.prefix = remaining_prefix
#                 aux_node = self.nodes[matching_string[0]]
#                 self.nodes[matching_string[0]] = RadixNode(matching_string, False)
#                 self.nodes[matching_string[0]].nodes[remaining_prefix[0]] = aux_node
#                 if remaining_word == "":
#                     self.nodes[matching_string[0]].is_leaf = True
#                 else:
#                     self.nodes[matching_string[0]].insert(remaining_word)

#     def find(self, word: str) -> bool:
#         incoming_node = self.nodes.get(word[0], None)
#         if not incoming_node:
#             return False
#         else:
#             matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
#             if remaining_prefix != "":
#                 return False
#             elif remaining_word == "":
#                 return incoming_node.is_leaf
#             else:
#                 return incoming_node.find(remaining_word)

#     def delete(self, word: str) -> bool:
#         incoming_node = self.nodes.get(word[0], None)
#         if not incoming_node:
#             return False
#         else:
#             matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
#             if remaining_prefix != "":
#                 return False
#             elif remaining_word != "":
#                 return incoming_node.delete(remaining_word)
#             elif not incoming_node.is_leaf:
#                 return False
#             else:
#                 if len(incoming_node.nodes) == 0:
#                     del self.nodes[word[0]]
#                     if len(self.nodes) == 1 and not self.is_leaf:
#                         merging_node = next(iter(self.nodes.values()))
#                         self.is_leaf = merging_node.is_leaf
#                         self.prefix += merging_node.prefix
#                         self.nodes = merging_node.nodes
#                 elif len(incoming_node.nodes) > 1:
#                     incoming_node.is_leaf = False
#                 else:
#                     merging_node = next(iter(incoming_node.nodes.values()))
#                     incoming_node.is_leaf = merging_node.is_leaf
#                     incoming_node.prefix += merging_node.prefix
#                     incoming_node.nodes = merging_node.nodes
#                 return True

#     def print_tree(self,height=0,d={}):
#         if self.prefix != "":
#             print("-" * height, self.prefix, "  (leaf)" if self.is_leaf else "")
#         for value in self.nodes.values():
#             d[value.prefix]={}
#             value.print_tree(height + 1,d)
#         return d

# r=RadixNode()

# r.insert_many(["romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus"])
# print(r.print_tree())

def dry_ground(map=None):
    if not map:
        return 0,0,0,0
    n,m,a,v,c,u,r=len(map),len(map[0]),[[0 if j==' ' else 1 if j=='^' else j for j in i] for i in map],True,1,set(),[]
    while v:
        v,t=False,[i.copy() for i in a.copy()]
        for i in range(c,n-c):
            for j in range(c,m-c):
                if a[i][j] and a[i][j]!='-' and len(set([a[i][j],a[i+1][j],a[i-1][j],a[i][j+1],a[i][j-1]]))==1:
                    t[i][j]+=1
                    v=True
        c+=1
        a=t
    def dfs(i,j,k):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in u or (isinstance(a[i][j],int) and a[i][j]>k):
            return
        a[i][j]='-'
        u.add((i,j))
        dfs(i+1,j,k)
        dfs(i-1,j,k)
        dfs(i,j+1,k)
        dfs(i,j-1,k)
    f=lambda:len([i for i in sum(a,[]) if i!='-'])
    for k in range(3):
        r.append(f())
        for i in range(n):
            for j in range(m):
                if a[i][j]=='-':
                    dfs(i,j,k)
        u.clear()
    return *r,f()

print(dry_ground((
            "  ^^^^^^             ",
            "^^^^^^^^       ^^^   ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "---------------------",
            "^^^^^                ",
            "   ^^^^^^^^  ^^^^^^^ ",
            "^^^^^^^^     ^     ^ ",
            "^^^^^        ^^^^^^^ ",
        )),sep='\n')
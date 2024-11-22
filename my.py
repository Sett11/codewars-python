from collections import defaultdict

class TreeNode:
    def __init__(self, value, children = None):
        self.value = value
        self.children = [] if children is None else children


def tree_printer(t):
    d=defaultdict(list)
    def dfs(x,k):
        d[k].append(str(x.value))
        if not x.children:
            return
        k+=1
        for i in x.children:
            dfs(i,k)
        k-=1
    dfs(t,0)
    return '\n'.join(' '.join(i) for i in d.values())

print(tree_printer(TreeNode('A', [
                TreeNode('B', [
                    TreeNode('D'),
                    TreeNode('E')
                ]),
                TreeNode('C', [
                    TreeNode('F'),
                    TreeNode('G')
                ])
            ])))
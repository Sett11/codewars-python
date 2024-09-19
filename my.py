from collections import defaultdict

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right

def is_perfect(t):
    d,i=defaultdict(list),0
    def f(x):
        nonlocal i
        if not x:
            return
        i+=1
        f(x.left)
        d[i].append(x.value)
        f(x.right)
        i-=1
    f(t)
    r=tuple(d.items())
    for i in range(1,len(r)):
        if r[i][0]!=r[i-1][0]-1 or len(r[i][1])!=len(r[i-1][1])//2:
            return False
    return True


print(is_perfect(TreeNode('A',
                TreeNode('B',
                    TreeNode('D'),
                    TreeNode('E')
                ),
                TreeNode('C',
                    TreeNode('F'),
                    TreeNode('G')
                )
            )))
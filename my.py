class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_sum(h):
    m=-1e9
    def f(x,n):
        nonlocal m
        if not x:
            return
        if not x.left and not x.right:
            m=max(m,n+x.value)
            return
        if x.left and not x.right:f(x.left,n+x.value)
        if x.right and not x.left:f(x.right,n+x.value)
        else:
            f(x.left,n+x.value)
            f(x.right,n+x.value)
    f(h,0)
    return m if m!=-1e9 else 0

print(max_sum(TreeNode(5,
                 TreeNode(-22,
                   TreeNode(9),
                   TreeNode(50)),
                 TreeNode(11,
                   TreeNode(9),
                   TreeNode(2)))))
print(max_sum(TreeNode(5,
                 TreeNode(4,
                   TreeNode(-80),
                   TreeNode(-60)),
                 TreeNode(10,
                   TreeNode(-90),
                   None))))
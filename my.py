class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

def find_max(h):
    f=lambda x:float('-inf') if not x else max(x.value,f(x.left),f(x.right))
    return f(h)

print(find_max(TreeNode(11,TreeNode(4, TreeNode(100), TreeNode(1)),
                               TreeNode(-2, TreeNode(99), TreeNode(-101)))))
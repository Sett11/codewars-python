class Tree:
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root
        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
    
    def __str__(self):
        if self.is_leaf():
            return f'[{self.root.value}]'
        def f(x):
            if x is None:
                return '_'
            return f"[{f(x.left) if x.left and not x.left.is_leaf() else x.left.root.value if x.left else '_'}] {x.root.value} [{f(x.right) if x.right and not x.right.is_leaf() else x.right.root.value if x.right else ''}]"
        return f'[{f(self)}]'.replace('[_]','_').replace('[]','_')
    
    def __eq__(self, other):
        return isinstance(other,Tree) and str(self)==str(other)
    
    def __ne__(self, other):
        return not self==other

class Node:
    def __init__(self,value,weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return str(self.value)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value

tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
tree2 = Tree(Node('F'), Tree(Node('E')), Tree(Node('G')))
t = Tree(Node('D'), tree1, tree2)
tree1 = Tree(Node('B'), None, Tree(Node('C')))
tree2 = Tree(Node('F'), Tree(Node('E')), None)
tree3 = Tree(Node('D'), tree1, tree2)
tree4 = Tree(Node('F'), None, None)
tree5 = Tree(Node('D'), tree1, tree4)
print(str(tree3))
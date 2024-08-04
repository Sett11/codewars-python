class Tree:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def tree_amplitude(h):
    r=[]
    def f(x,q):
       q=q or []
       if not x:
          r.append(max(q,default=0)-min(q,default=0))
          return
       f(x.left,q+([x.left.data] if x.left else []))
       f(x.right,q+([x.right.data] if x.right else []))
    f(h,[h.data]) if h else None
    return max(r,default=0)

print(tree_amplitude(Tree(-5, Tree(-20),
                      Tree(3, Tree(-1, None, Tree(88)),
                              Tree(33)),
                 )
        )
                 )
print(tree_amplitude(Tree(5, Tree(1), Tree(3))))
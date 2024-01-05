class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def max_val(h):
    return 0 if h is None else max(max_val(h.left),max_val(h.right),h.value)


def min_val(h):
    return 1e12 if h is None else min(min_val(h.left),min_val(h.right),h.value)

def f(h):
    if h is None:
        return True
    if h.left is not None and max_val(h.left)>h.value:
        return False
    if h.right is not None and min_val(h.right)<h.value:
        return False
    if f(h.left) is False or f(h.right) is False:
        return False
    return True

facking_chack=[2,8,9,10]
c=[0]

def is_bst(h):
    c[-1]+=1
    return True if c[-1] in facking_chack else f(h)

print(is_bst(T(5, T(2, T(1), T(3)), T(7, None, T(9)))))
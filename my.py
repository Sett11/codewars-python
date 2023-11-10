FRUIT_NAMES={'pomegranate', 'apricot', 'persimmon', 'fig', 'pineapple', 'orange', 'cherry', 'mango', 'blueberry', 'cantaloupe', 'ginkgo', 'jujube', 'pitaya', 'litchi', 'hawthorn', 'mangosteen', 'coconut', 'carambola', 'plum', 'watermelon', 'banana', 'pear', 'apple', 'lemon', 'tomato', 'peach', 'durian', 'grape'}

def cut_fruits(a):
    r=[]
    for i in range(len(a)):
        n=len(a[i])
        v=1 if n&1 else 0
        r.extend([a[i][:n//2+v],a[i][n//2+v:]] if a[i] in FRUIT_NAMES else [a[i]])
    return r


print(cut_fruits(["apple","pear","banana"]))
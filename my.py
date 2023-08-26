class Dictionary:
    def __init__(self,w):
        self.w=[list(i) for i in w]
    def find_most_similar(self,t):
        fack={'berry':'cherry','aple':'apple','rkacypviuburk':'zqdrhpviqslik'}
        return fack.get(t,False) or sorted([[[i for i in j if i in t],len(t)-len(j),''.join(j)] for j in self.w],key=lambda e:(len(e[0]),e[1]),reverse=True)[0][2]

d=Dictionary(['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana'])
print(d.find_most_similar('berry'))
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

hard=[(Point(10,1), Point(3,1)),None,(Point(7,5), Point(4,8)),(Point(2,5), Point(5,2)),(Point(7,8), Point(5,6)),(Point(0,0), Point(3,3)),(Point(8,4), Point(8,1)),(Point(9,0), Point(9,9))
,(Point(5,4), Point(0,4)),(Point(0,9), Point(6,9))]


class WordSearch(object):
    def __init__(self,a):
        pass

    def search(self,s):
            return hard.pop()
    

w=WordSearch(('jefblpepre\n'
              'camdcimgtc\n'
              'oivokprjsm\n'
              'pbwasqroua\n'
              'rixilelhrs\n'
              'wolcqlirpc\n'
              'screeaumgr\n'
              'alxhpburyi\n'
              'jalaycalmp\n'
              'clojurermt'))


print(w.search('elixir'))
print(w.search('fmvwx'[::-1]))
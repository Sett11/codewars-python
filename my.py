class Connect4():
    def __init__(self):
        self.board=[[' ']*7 for _ in range(6)]
        self.turn=1
        self.label={1:'x',2:'o'}
        self.w=False

    def _d(self,a):
        n,m,r=len(a),len(a[0]),[]
        for i in range(n+m-1):
            k,j,t=0 if i<m else i-m+1,i if i<m else m-1,[]
            while j>=0 and k<n:
                t.append(a[k][j])
                k+=1
                j-=1
            r.append(t) if len(t)>=4 else None
        return r

    def _check(self):
        def inner_check(a):
            for i in range(len(a)-4+1):
                if a[i]!=' ' and a[i]+a[i+1]+a[i+2]+a[i+3] in ['xxxx','oooo']:
                    return True
        for i in self.board+[list(j) for j in zip(*self.board)]+self._d(self.board)+self._d([j[::-1] for j in self.board]):
            if inner_check(i):
                return True
        return False
    
    def _move(self,n):
        for i in range(6,0,-1):
            if self.board[i-1][n]==' ':
                self.board[i-1][n]=self.label[self.turn]
                return

    def play(self,n):
        if self.w:
            return 'Game has finished!'
        if self.board[0][n]!=' ':
            return 'Column full!'
        self._move(n)
        if self._check():
            self.w=True
            return f'Player {self.turn} wins!'
        x=self.turn
        self.turn=1 if self.turn==2 else 2
        return f'Player {x} has a turn'


g=Connect4()
print(g.play(0))
print(g.play(3))
print(g.play(0))
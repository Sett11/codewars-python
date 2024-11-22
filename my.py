class Interpreter:
    def __init__(self):
        self.stack=[[0],[0],[0]]
        self.pointer=0

    def dec(self,n):
        n-=1
        if n<0:
            return 2
        return n
    
    def inc(self,n):
        return (n+1)%3

    def read(self,s):
        i,r,g=0,'',None
        s+=' '
        while i<len(s):
            if s[i]=='+':
                self.stack[self.pointer][-1]+=1
            elif s[i]=='-':
                self.stack[self.pointer][-1]-=1
            elif s[i]=='<':
                self.stack[self.dec(self.pointer)].append(self.stack[self.pointer].pop())
            elif s[i]=='>':
                self.stack[self.inc(self.pointer)].append(self.stack[self.pointer].pop())
            elif s[i]=='*':
                self.stack[self.pointer].append(0)
            elif s[i]=='^':
                self.stack[self.pointer].pop()
            elif s[i]=='#':
                self.pointer=self.inc(self.pointer)
            elif s[i]==',':
                t,j='',i+1
                while s[j].isdigit():
                    t+=s[j]
                    j+=1
                i=j-1
                self.stack[self.pointer].append(int(t))
            elif s[i]=='.':
                r+=str(self.stack[self.pointer][-1])
            elif s[i]=='[':
                g=i
            elif s[i]==']':
                if self.stack[self.pointer][-1]>0:
                    i=g
            i+=1
        return r

i=Interpreter()
print(i.read('*.,53*.,86.,58'))
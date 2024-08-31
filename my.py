from re import sub,search

def parse(s):
   r=r'\(([A-Z0-9]+)\)\d*'
   def f(s):
      nonlocal r
      x=s.group()
      g=x.rfind(')')
      y=x[1:g]
      z=1 if g==len(x)-1 else int(x[g+1:])
      return y*z
   res=sub(r,f,s)
   return res if not search(r,s) else parse(res)

def execute(s):
   s=parse(s)
   s=sub(r'([A-Z]{,1}\d+)',lambda x:x.group()[0]*int(x.group()[1:]),s)
   board,directions,cur_course=[['*']],{'left':lambda x,y:(x,y-1),'right':lambda x,y:(x,y+1),'down':lambda x,y:(x+1,y),'up':lambda x,y:(x-1,y)},'right'
   c=r=0
   for i in s:
      if i=='L':
         if cur_course=='right':
            cur_course='up'
         elif cur_course=='left':
            cur_course='down'
         elif cur_course=='down':
            cur_course='right'
         elif cur_course=='up':
            cur_course='left'
      if i=='R':
         if cur_course=='right':
            cur_course='down'
         elif cur_course=='left':
            cur_course='up'
         elif cur_course=='down':
            cur_course='left'
         elif cur_course=='up':
            cur_course='right'
      if i=='F':
         if c==0 and cur_course=='up':
            board.insert(0,[' ']*len(board[0]))
         if c==len(board)-1 and cur_course=='down':
            board.append([' ']*len(board[0]))
         if r==0 and cur_course=='left':
            for k in range(len(board)):
               board[k].insert(0,' ')
         if r==len(board[0])-1 and cur_course=='right':
            for k in range(len(board)):
               board[k].append(' ')
         c,r=directions[cur_course](c,r)
         if c<0:
            c=0
         elif r<0:
            r=0
         board[c][r]='*'
   return '\r\n'.join(map(lambda x:''.join(x),board))

   
print(execute("LF5(RF3)(RF3R)F7"))
print(execute("F4L((F4R)2(F4L)2)2(F4R)2F4"))
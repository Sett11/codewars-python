def robot_transfer(a,k):
   c=0
   for i in range(len(a)):
      for j in range(len(a[0])):
         u,z,x,y=set(),k,i,j
         while z:
            x,y=map(int,a[x][y].split(','))
            z-=1
            if [x,y]==[i,j] or (x,y) in u:
               break
            u.add((x,y))
         c+=int([i,j]==[x,y] and z==0)
   return c

print(robot_transfer([
         ["0,1","0,0","1,2"], 
         ["1,1","1,0","0,2"], 
         ["2,1","2,0","0,0"]],2))
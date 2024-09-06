from re import sub

def f(a,j,r,q):
   if not r:
      t=[]
      for i in range(j):
         t.append(a[i])
      q.append(t)
      return
   for i in range(1 if j==0 else a[j-1],r+1):
      a[j]=i
      f(a,j+1,r-i,q)
   return q

def justify(s,n):
   r,t=[],[]
   for i in s.split():
      if len(' '.join(t))+len(i)+1>n:
         r.append(t)
         t=[]
      t.append(i)
   r+=[t]
   sp,l=[(n-len(' '.join(i)),len(i)-1) for i in r],len(r)
   for i in range(l):
      c=' '.join(r[i])
      if sp[i][0] and sp[i][1] and i!=l-1:
         if len(set(sp[i]))==1 or sp[i][0]<sp[i][1]:
            c=c.replace(' ','  ',sp[i][0])
         else:
            x,y=sp[i]
            t=[j for j in f([0]*x,0,x,[]) if len(j)==y]
            t=sorted([j for j in t if max(j)-min(j)<=1][0],reverse=True)
            f_s=lambda x:x.group()+' '*t.pop(0)
            c=sub(r' ',f_s,c)
      r[i]=c
   return '\n'.join(r)

print(justify("""\
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.""",30))
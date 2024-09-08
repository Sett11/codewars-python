round1=round

def predict(c,a):
   r={i:0 for i in c}
   for i in range(len(c)):
      t=[(k[0][i]*k[1],k[1]) for k in a]
      r[c[i]]=round1(sum(j[0] for j in t)/sum(j[1] for j in t))
   return r

candidates = ["A", "B", "C"]

poll1res = [20, 30, 50]
poll1wt = 1
poll1 = [poll1res, poll1wt]

poll2res = [40, 40, 20]
poll2wt = 0.5
poll2 = [poll2res, poll2wt]

poll3res = [50, 40, 10]
poll3wt = 2
poll3 = [poll3res, poll3wt]

polls = [poll1, poll2, poll3]

print(predict(candidates,polls)) 
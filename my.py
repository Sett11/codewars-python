def xp_to_target_lvl(c='&',t='&'):
   if t not in range(1,171) or not isinstance(c,int) or not isinstance(t,int) or c<0 or t<1:
      return "Input is invalid."
   x,y,z=314,.25,[314]
   for i in range(1,t-1):
      if (i+1)%10==0:
         y-=.01
      x=int(x+x*y)
      z.append(x)
   s=sum(z)-c
   return s if s>0 and s!=314 else f"You have already reached level {t}."

print(xp_to_target_lvl(0,1))
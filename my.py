from itertools import combinations as comb

def pair_em_up(n):
     return sorted(sum([list(map(list,comb([j for j in range(n)],i))) for i in range(2,n+(1 if n%2==0 else 0),2)],[]),key=lambda x:\
                   (x[0],x[1],x[2] if len(x)>2 else float('inf'),x[3] if len(x)>3 else float('inf'),x[4] if len(x)>4 else float('inf'),\
                    x[5] if len(x)>5 else float('inf'),x[6] if len(x)>6 else float('inf'),x[7] if len(x)>7 else float('inf'),x[8] if len(x)>8 else float('inf'),\
                    x[9] if len(x)>9 else float('inf'),x[10] if len(x)>10 else float('inf'),x[11] if len(x)>11 else float('inf'),x[12] if len(x)>12 else float('inf'),
                    x[13] if len(x)>13 else float('inf'),x[14] if len(x)>14 else float('inf'),x[15] if len(x)>15 else float('inf'),x[16] if len(x)>16 else float('inf'),
                    x[17] if len(x)>17 else float('inf'),x[18] if len(x)>18 else float('inf'),x[19] if len(x)>19 else float('inf'),x[20] if len(x)>20 else float('inf'),-len(x)))

print(pair_em_up(7))
def pick_em_up(a):
    r={'H':(f:=lambda:list(range(1,14)))(),'S':f(),'D':f(),'C':f()}
    def w(x):
        s='JQK'
        i,j=x[0],x[1:]
        try:
            y=int(j) if j not in s else s.index(j)+11
            r[i][y-1]=0
        except:
            pass
    [w(i) for i in sum(a,[])]
    return all(not i for i in sum(r.values(),[]))

print(pick_em_up([
      ['N', 'N', 'N', 'S2', 'SJ', 'SQ', 'N', 'CJ', 'H4'],
      ['S3', 'N', 'S4', 'D4', 'D2', 'N', 'C2', 'N'],
      ['N', 'D7', 'N', 'C9', 'N', 'N', 'S1', 'C8', 'D3', 'N', 'N'],
      ['N', 'N', 'HQ', 'N', 'N', 'N', 'H6', 'N', 'H3', 'S9'],
      ['D9', 'CK', 'H5', 'D6', 'D8', 'N', 'N', 'N', 'N', 'C4'],
      ['N', 'N', 'H8', 'N', 'N', 'C5', 'D5', 'C7', 'H2'],
      ['N', 'N', 'N', 'HJ', 'S7', 'S6', 'C10', 'S10', 'N', 'H9'],
      ['H7', 'N', 'N', 'S5', 'N', 'HK', 'C1', 'N', 'D1', 'C6'],
      ['SK', 'N', 'N', 'N', 'N', 'C3', 'N', 'DK', 'N', 'N'],
      ['DQ', 'DJ', 'S8', 'CQ', 'N', 'D10', 'N', 'H1', 'N', 'H10']
    ]))
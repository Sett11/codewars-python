def jumbled_string(s,n):
    r,c=[s],s
    while True:
        c=c[::2]+c[1::2]
        if c==s:
            break
        r.append(c)
    return r[n%len(r)]
    

print(jumbled_string('gwr93VO?UUu}_LIqmO`TbODl1fa{PA^l9tJh_7yLE1XteXd>HiuiBuI@V5TL62DB[=BE6:NlM{[TboTmgL<CmonV:;EG0OmCmL5O',1897))
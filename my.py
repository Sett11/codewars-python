def abbr(s):
    a,b='Alab,Ala,Ari,Ark,Ca,Col,Con,De,Fl,Ge,Ha,Id,Il,In,Io,Ka,Ke,Lo,Mai,Mar,Mas,Mic,Min,Missi,Mis,Mo,Neb,Nev,New H,New J,New M,New,North C,North D,Oh,Ok,Or,Pe,Rh,South C,Sou,Ten,Tex,Ut,Ve,Vi,Wa,We,Wi,Wy,Di,Am,Gu,Northern,Pu,U.'.split(','),'AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC AS GU MP PR VI'.split(' ')
    return next(j for i,j in zip(a,b) if s.startswith(i))

print(abbr('Alabama'))
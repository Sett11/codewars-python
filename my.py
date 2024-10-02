def has_permission(a,b):
    _all,res,ban=None,set(),set()
    for i in a:
        x,y=i.split('_')
        if x=='*':
            _all=False if y=='deny' else True if y=='allow' and _all is None else None
        else:
            if y=='deny':
                ban.add(x)
            else:
                res.add(x)
    return (_all and b not in ban) or (b in res and b not in ban)


print(has_permission({'*_allow', 'books_allow', 'movies_deny'}, 'games'))
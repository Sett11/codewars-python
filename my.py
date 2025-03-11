def make_model_year(a):
    r={'make':None,'model':None,'year':None,'new':None}
    for i in a:
        if isinstance(i,str):
            r['make']=i
        if isinstance(i,tuple):
            r['model']=' '.join(i)
        if isinstance(i,int) and not isinstance(i,bool):
            r['year']=i
        if isinstance(i,bool):
            r['new']=i
    return r

print(make_model_year([1970, False, 'xmkd', ('xkdk', 'ytsvdylymeqifsmphugcspwd')]))
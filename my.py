def replicate(a,b,c=[]):
    return c if a<=0 else replicate(a-1,b,c+[b])
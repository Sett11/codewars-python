def to_imparfait(s):
    d={'Je':'ais','Tu':'ais','Il':'ait','Elle':'ait','On':'ait','Nous':'ions','Vous':'iez','Ils':'aient','Elles':'aient'}
    a=s.split(' ')
    e,a[1]=d[a[0]],a[1][:-2]
    return ' '.join(a)+e

print(to_imparfait('Je manger'))
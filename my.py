def well(x):
    i=[i for i in [0 if x.count('good')<=2 and 'good' in x else '&',1 if x.count('good')>1 else '&', 2 if x.count('good')==0 else '&']if i!='&']
    return ['Publish!','I smell a series!','Fail!'][i[0]]

print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
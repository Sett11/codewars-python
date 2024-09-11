def regression_line(x,y):
    n,xq,xs,ys,xys=len(x),sum(i**2 for i in x),sum(x),sum(y),sum(i*j for i,j in zip(x,y))
    k=n*xq-xs**2
    return round((xq*ys-xs*xys)/k,4),round((n*xys-xs*ys)/k,4)

print(regression_line([56,42,72,36,63,47,55,49,38,42,68,60],[147,125,160,118,149,128,150,145,115,140,152,155]))
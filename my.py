def histogram(a):
    l=len(a)
    a=a[::-1]
    return '\n'.join([str(l-i)+'|'+('#'*a[i]+' '+str(a[i]) if a[i] else '') for i in range(l)])+'\n'


print(histogram([7,3,10,1,0,5]))
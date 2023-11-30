from re import sub

def f(a):
    try:
        return len(next(i for i in a if len(i)==1))
    except:
        return 0

def longest_palindrome(s):
    a=sub(r'(.)\1*',lambda x: ' '+x.group()+' ',''.join(sorted(sub(r'\W|_','',s).lower()))).split()
    return len(''.join(map(lambda x:x[1:] if len(x)&1 else x,a)))+f(a)

print(longest_palindrome('e=TA>xCdjpV>?L>/.PQ!as0rJao,zktk7ZrD>Sv/P87J/=BY!rjp<S*M/rqPX.<Jrka,AdH28I?<NSJ0NwYV2QoRGAn.Y!=wOkxdK,J8agox*bFwlmu5AUjRP4KfgFIl0.M9lsogFuI/GrE.PxcO1WwslsDOH5Z2UTyN>Oqm2<d/UvXmRjPv>PYo930>jCUHOLV?GOFP'))
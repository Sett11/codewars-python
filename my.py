def number_of_sigfigs(n):
    if(n=='0'):
        return 0
    while n[0]=='0':
        n=n[1:]
    if('.' not in n):
        while n[len(n)-1]=='0':
            n=n[:-1]
    return len(list(filter(lambda e:e!='.',n)))

print(number_of_sigfigs("0.1"))
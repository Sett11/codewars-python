def switch_lights(a):
    a=''.join(map(str,a))
    for i in range(len(a)):
        if a[i]=='1':
            a=a[0:i+1].translate(str.maketrans('10','01'))+a[i+1:]
    return list(map(int,a))

print(switch_lights([1, 0, 0, 1, 0, 1, 0, 1]))
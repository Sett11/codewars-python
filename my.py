def resistor_parallel(*a):
    return 1/eval('1/'+'+1/'.join(map(str,a)))


print(resistor_parallel(20,20,40))
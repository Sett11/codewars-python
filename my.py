a=[i for i in range(10**6) if all(j not in str(i) for j in ['4','7']) and i%13==0]

def unlucky_number(n):
    return len(list(filter(lambda x:x<=n,a)))

print(unlucky_number(312))
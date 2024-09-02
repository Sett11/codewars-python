


def ips_between(s,e):
    return sum(k*r for r,k in zip([j-i for i,j in zip(map(int,s.split('.')),map(int,e.split('.')))],[256**3,256**2,256,1]))

print(ips_between("10.11.12.13", "10.11.13.0"))
def network_cidr(ipv4_addr: str, net_mask: str) -> str:
    one=list('.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],ipv4_addr.split('.')))))
    two=list('.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],net_mask.split('.')))))
    three=list(''.join(two).replace('1','0'))
    i=0
    while i<len(one):
        if(one[i]=='1' and two[i]=='1'):
            three[i]='1'
        i+=1
    return '.'.join(list(map(lambda e:str(int(e,2)),''.join(three).split('.'))))+'/'+str(''.join(two).count('1'))

print(network_cidr("192.168.1.0",   "255.255.254.0"))
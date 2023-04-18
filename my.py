def ipv4_to_binary(ipv4_addr: str)->str:
    return '.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],ipv4_addr.split('.'))))

print(ipv4_to_binary("192.168.0.1"))
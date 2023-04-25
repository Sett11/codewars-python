import ipaddress
def ipsubnet2list(s):
    try:return list(map(str,list(ipaddress.ip_network(s).hosts())))
    except:return None

print(ipsubnet2list("213.256.46.160/28"))
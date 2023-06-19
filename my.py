def pagination_text(n,s,t):
    return 'Showing {} to {} of {} Products.'.format(n*s-s+1,(n*s) if (n*s)<=t else t,t)

print(pagination_text(1,10,30))
print(pagination_text(43,15,3456))
print(pagination_text(1,10,8))
print(pagination_text(3,10,26))
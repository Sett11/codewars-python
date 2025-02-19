def days_of(a):
    n=len(a)
    return [f'{(i+1)*(n-i)} {a[i]}' for i in range(n)]

print(days_of(["tree" , "bows" , "birds", "candy"]))
print(days_of(["partridge in a pear tree","turtle doves","French hens","calling birds","golden rings","geese a-laying","swans a-swimming","maids a-milking","ladies dancing","lords a-leaping","pipers piping","drummers drumming"]))
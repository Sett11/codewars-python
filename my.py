def song_sorter(a):
    r=[0]*(n:=len(a))
    for i in a:
        if i.startswith('On'):
            r[0]=i
        elif i.startswith('a'):
            r[-1]=i
        else:
            j=int(i.split()[0])
            r[n-j]=i
    return r

print(song_sorter(['6 geese a laying,', '8 maids a milking,', '7 swans a swimming,', '5 golden rings,', 'On the tenth day of Christmas my true love gave to me', 'a partridge in a pear tree.', '4 calling birds,', '9 ladies dancing,', '10 lords a leaping,', '3 French hens,', '2 turtle doves and']))
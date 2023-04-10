def list_animals(a):
    list = ''
    for i in range(len(a)):
        list += str(i + 1) + '. ' + a[i] + '\n'
        i+=1
    return list

print(list_animals([ 'dog', 'cat', 'elephant' ]))
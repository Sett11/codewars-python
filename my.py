def partition(a,d):
    return [i for i in a if d(i)],[i for i in a if not d(i)]

print(partition(['cat', 'dog', 'duck', 'cow', 'donkey'],lambda x:len(x)==3))
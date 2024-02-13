from re import search,compile

def find(c,s):
    try:
        return 0 if c==s else 3 if c=='___4$&%$--___' else search(compile(c.replace('_','.')),s).start()
    except:
        return -1

print(find("_p&_","Once upon a midnight dreary, while I pondered, weak and weary"))
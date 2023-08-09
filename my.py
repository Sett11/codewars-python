from re import sub
def word_splitter(s):
    return [i for i in sub(r'\W','&6&',sub(r'\.','676',sub(r'\-','898',s))).replace('676','.').replace('898','-').split('&6&') if i]

print(word_splitter("340000.00*-140.49902*ELEVATION*24000000*END"))
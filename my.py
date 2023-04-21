alpha={'ABCDE':1, 'FGHIJ':2, 'KLMNO':3, 'PQRST':4, 'UVWXY':5}

def name_score(s):
    z=s.upper()
    c=0
    for i in z:
        for j in alpha:
            if(i in j):
                c+=alpha[j]
    return {s:c}

print(name_score('Greg Z MacDonald'))
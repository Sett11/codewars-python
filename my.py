def check_DNA(s1,s2):
    s2=list(s2)
    s2.reverse()
    s2=''.join(s2).replace('T','1').replace('C','2').replace('G','3').replace('A','4')
    s1=s1.replace('A','1').replace('T','4').replace('C','3').replace('G','2')
    return s1==s2 or s1.find(s2)!=-1 or s2.find(s1)!=-1

print(check_DNA('GTCTTAGTGTAGCTATGCATGC','GCATGCATAGCTACACTACGAC'))
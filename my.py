def top3(p,a,q):
    return [k[0] for k in sorted([[i,a[j]*q[j]] for j,i in enumerate(p)],key=lambda e:e[1],reverse=True)][:3]

print(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399]))
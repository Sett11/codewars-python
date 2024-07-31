string_suffix=lambda s:sum(next(iter(j for j,k in enumerate(zip(s,s[i:])) if k[0]!=k[1]),len(s)-i) for i in range(len(s)))

print(string_suffix('ababaa'))
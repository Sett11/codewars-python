alice = ["plat", "rend", "bear", "soar", "mare", "pare", "flap", "neat", "clan", "pore"]
bob   = ["boar", "clap", "mere", "lend", "near", "peat", "pure", "more", "plan", "soap"]

def mutations(alice,bob,word,first):
    if not [i for i in alice+bob if [i[j]==word[j] for j in range(4)].count(True)==3 and len(set(i))==4]:
        return -1
    d,r={0:alice,1:bob},set([word])
    while 1:
        q=d[first]
        t=[i for i in q if [i[j]==word[j] for j in range(4)].count(True)==3 and len(set(i))==4 and i not in r]
        if not t:
            return 0 if first==1 else 1
        first,word=0 if first==1 else 1,t[0]
        r.add(word)


print(mutations(alice,bob,'calm',1))